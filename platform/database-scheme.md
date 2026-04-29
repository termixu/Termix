# 🗄️ СХЕМА БАЗЫ ДАННЫХ TERMIX ACADEMY

> **Версия:** 1.0
>
> **Дата:** Апрель 2026
>
> **СУБД:** PostgreSQL 15+
>
> **ORM:** SQLAlchemy + Alembic
>
> **Назначение:** Полная схема базы данных платформы Termix Academy

---

## 🧠 ФИЛОСОФИЯ СХЕМЫ

База данных Termix Academy спроектирована так, чтобы поддерживать:

- Управление пользователями (ученики, наставники, админы).
- Структуру курсов (курсы → модули → уроки).
- Прогресс учеников (какие уроки пройдены, с каким результатом).
- Систему геймификации (баджи, достижения, жетоны).
- Систему «Сбои Ядра» (предупреждения и инциденты).
- Взаимодействие с Termix AI (логи диалогов).
- Платежи и подписки.

Всё в одной нормализованной схеме.

---

## 👥 ПОЛЬЗОВАТЕЛИ — users

Хранит всех пользователей платформы.

- `id` — UUID, первичный ключ.
- `telegram_id` — BigInteger, уникальный, для связи с Telegram-ботом.
- `username` — VARCHAR(50), уникальный, not null.
- `display_name` — VARCHAR(100), not null (пиратское имя).
- `email` — VARCHAR(255), уникальный.
- `password_hash` — VARCHAR(255), NULL если вход только через Telegram.
- `role` — VARCHAR(20), not null, default 'student'. Возможные значения: 'student', 'mentor', 'admin', 'captain'.
- `rank` — VARCHAR(20), not null, default 'cabin_boy'. Возможные значения: 'cabin_boy', 'boatswain', 'navigator', 'cap', 'legend'.
- `xp` — INTEGER, not null, default 0.
- `coins` — INTEGER, not null, default 0 (внутренняя валюта).
- `avatar_sprites` — JSONB (настройки внешнего вида Termix'а).
- `streak_days` — INTEGER, default 0 (серия дней входа).
- `total_lessons_completed` — INTEGER, default 0.
- `total_projects_completed` — INTEGER, default 0.
- `last_activity_at` — TIMESTAMPTZ.
- `created_at` — TIMESTAMPTZ, not null, default NOW().
- `updated_at` — TIMESTAMPTZ, not null, default NOW().

Индексы: по `role`, по `rank`, по `xp DESC`, по `telegram_id` (частичный, где не NULL).

---

## 🎓 КУРСЫ — courses

Хранит информацию о всех курсах.

- `id` — UUID, первичный ключ.
- `slug` — VARCHAR(100), уникальный, not null (например: 'python-pirate-12').
- `title` — VARCHAR(200), not null.
- `subtitle` — VARCHAR(300).
- `description` — TEXT.
- `age_group` — VARCHAR(10), not null. Возможные значения: '10-11', '12-13', '14+'.
- `difficulty` — VARCHAR(10), not null, default 'easy'. Возможные значения: 'easy', 'medium', 'hard', 'legendary'.
- `cover_image_url` — VARCHAR(500).
- `order_num` — INTEGER, not null, default 0.
- `is_published` — BOOLEAN, not null, default FALSE.
- `termix_intro_text` — TEXT (что Termix говорит при старте курса).
- `estimated_hours` — INTEGER.
- `created_by` — UUID, ссылка на `users.id`.
- `created_at` — TIMESTAMPTZ, not null, default NOW().
- `updated_at` — TIMESTAMPTZ, not null, default NOW().

Индексы: по `age_group`, по `is_published` (частичный), по `order_num`.

---

## 📦 МОДУЛИ — modules

Хранит модули внутри курса.

- `id` — UUID, первичный ключ.
- `course_id` — UUID, not null, ссылка на `courses.id` с каскадным удалением.
- `title` — VARCHAR(200), not null.
- `slug` — VARCHAR(100), not null.
- `description` — TEXT.
- `badge_id` — UUID, ссылка на `badges.id` (бадж за завершение модуля).
- `order_num` — INTEGER, not null, default 0.
- `is_bonus` — BOOLEAN, not null, default FALSE (секретный модуль).
- `unlock_condition` — JSONB (условие открытия, например: {"xp": 500}).
- `created_at` — TIMESTAMPTZ, not null, default NOW().

Уникальность: (`course_id`, `order_num`).

Индексы: по `course_id`, по (`course_id`, `order_num`).

---

## 📖 УРОКИ — lessons

Хранит отдельные уроки внутри модуля.

- `id` — UUID, первичный ключ.
- `module_id` — UUID, not null, ссылка на `modules.id` с каскадным удалением.
- `title` — VARCHAR(200), not null.
- `slug` — VARCHAR(100), not null.
- `lesson_type` — VARCHAR(20), not null, default 'theory'. Возможные значения: 'theory', 'practice', 'quiz', 'project', 'boss_fight'.
- `content` — JSONB, not null, default '{}' (вся теория, задания, сцены Spline, мемы Termix'а).
- `xp_reward` — INTEGER, not null, default 50.
- `coins_reward` — INTEGER, not null, default 10.
- `estimated_minutes` — INTEGER, default 20.
- `order_num` — INTEGER, not null, default 0.
- `is_published` — BOOLEAN, not null, default FALSE.
- `created_at` — TIMESTAMPTZ, not null, default NOW().

Уникальность: (`module_id`, `order_num`).

Индексы: по `module_id`, по `lesson_type`.

---

## ✍️ ОТПРАВЛЕННЫЕ ЗАДАНИЯ — submissions

Хранит код или проекты, которые ученик отправляет на проверку.

- `id` — UUID, первичный ключ.
- `user_id` — UUID, not null, ссылка на `users.id` с каскадным удалением.
- `lesson_id` — UUID, not null, ссылка на `lessons.id` с каскадным удалением.
- `code_text` — TEXT (код, который написал ученик).
- `file_url` — VARCHAR(500) (ссылка на проект Spline, GitHub).
- `status` — VARCHAR(20), not null, default 'pending'. Возможные значения: 'pending', 'auto_checked', 'passed', 'failed', 'mentor_review'.
- `score` — INTEGER, от 0 до 100.
- `auto_feedback` — JSONB (автоматическая проверка).
- `mentor_feedback` — TEXT (ручная проверка наставником).
- `mentor_id` — UUID, ссылка на `users.id`.
- `attempt_number` — INTEGER, not null, default 1.
- `submitted_at` — TIMESTAMPTZ, not null, default NOW().
- `reviewed_at` — TIMESTAMPTZ.

Индексы: по `user_id`, по `lesson_id`, по `status`, по (`user_id`, `lesson_id`).

---

## 📊 ПРОГРЕСС — user_progress

Хранит прогресс ученика по каждому уроку.

- `user_id` — UUID, not null, ссылка на `users.id` с каскадным удалением.
- `lesson_id` — UUID, not null, ссылка на `lessons.id` с каскадным удалением.
- `status` — VARCHAR(20), not null, default 'locked'. Возможные значения: 'locked', 'available', 'in_progress', 'completed', 'perfect'.
- `score` — INTEGER, default 0.
- `attempts` — INTEGER, default 0.
- `time_spent_seconds` — INTEGER, default 0.
- `termix_mood` — VARCHAR(20) (реакция Termix'а: proud, neutral, disappointed).
- `started_at` — TIMESTAMPTZ.
- `completed_at` — TIMESTAMPTZ.

Первичный ключ: (`user_id`, `lesson_id`).

Индексы: по (`user_id`, `status`).

---

## 📝 ЗАПИСИ НА КУРСЫ — enrollments

Хранит информацию о том, какой ученик на какой курс записан.

- `user_id` — UUID, not null, ссылка на `users.id` с каскадным удалением.
- `course_id` — UUID, not null, ссылка на `courses.id` с каскадным удалением.
- `progress_percent` — INTEGER, default 0, от 0 до 100.
- `status` — VARCHAR(20), not null, default 'active'. Возможные значения: 'active', 'paused', 'completed', 'dropped'.
- `enrolled_at` — TIMESTAMPTZ, not null, default NOW().
- `completed_at` — TIMESTAMPTZ.

Первичный ключ: (`user_id`, `course_id`).

---

## 🏆 БАДЖИ — badges

Хранит все возможные баджи.

- `id` — UUID, первичный ключ.
- `name` — VARCHAR(100), not null.
- `description` — TEXT.
- `image_url` — VARCHAR(500), not null (8-bit пиксельный значок).
- `rarity` — VARCHAR(10), not null, default 'common'. Возможные значения: 'common', 'rare', 'epic', 'legendary'.
- `category` — VARCHAR(30), not null. Возможные значения: 'module', 'skill', 'rank', 'event', 'secret'.
- `created_at` — TIMESTAMPTZ, not null, default NOW().

Индексы: по `rarity`.

---

## 🎖️ ДОСТИЖЕНИЯ — achievements

Хранит достижения и условия их получения.

- `id` — UUID, первичный ключ.
- `slug` — VARCHAR(50), уникальный, not null (например: 'first_commit').
- `name` — VARCHAR(100), not null.
- `description` — TEXT, not null.
- `emoji` — VARCHAR(10).
- `category` — VARCHAR(30), not null. Возможные значения: 'learning', 'coding', 'git', 'community', 'streak', 'secret'.
- `criteria` — JSONB, not null (условие получения, например: {"action": "complete_lessons", "count": 10}).
- `xp_reward` — INTEGER, not null, default 100.
- `coins_reward` — INTEGER, not null, default 50.
- `badge_id` — UUID, ссылка на `badges.id`.
- `is_hidden` — BOOLEAN, not null, default FALSE (секретное достижение).
- `created_at` — TIMESTAMPTZ, not null, default NOW().

Индексы: по `category`.

---

## 🏅 СВЯЗКИ БАДЖЕЙ И ДОСТИЖЕНИЙ — user_badges, user_achievements

**user_badges:**

- `user_id` — UUID, not null, ссылка на `users.id` с каскадным удалением.
- `badge_id` — UUID, not null, ссылка на `badges.id` с каскадным удалением.
- `earned_at` — TIMESTAMPTZ, not null, default NOW().
- `is_equipped` — BOOLEAN, not null, default FALSE.

Первичный ключ: (`user_id`, `badge_id`).

**user_achievements:**

- `user_id` — UUID, not null, ссылка на `users.id` с каскадным удалением.
- `achievement_id` — UUID, not null, ссылка на `achievements.id` с каскадным удалением.
- `earned_at` — TIMESTAMPTZ, not null, default NOW().
- `notified` — BOOLEAN, not null, default FALSE.

Первичный ключ: (`user_id`, `achievement_id`).

---

## 🐱 ЛОГИ TERMIX AI — termix_logs

Хранит все взаимодействия ученика с котом-помощником.

- `id` — UUID, первичный ключ.
- `user_id` — UUID, not null, ссылка на `users.id` с каскадным удалением.
- `lesson_id` — UUID, ссылка на `lessons.id`.
- `action_type` — VARCHAR(30), not null. Возможные значения: 'help_request', 'meme_shown', 'hint_given', 'error_explained', 'motivation', 'quiz_hint'.
- `user_prompt` — TEXT.
- `termix_response` — TEXT.
- `mood` — VARCHAR(10). Возможные значения: 'happy', 'sarcastic', 'worried', 'proud', 'joking'.
- `helpful` — BOOLEAN (оценка ученика).
- `created_at` — TIMESTAMPTZ, not null, default NOW().

Индексы: по `user_id`, по `action_type`, по `lesson_id`.

---

## ⚡ СБОИ ЯДРА — core_failures

Хранит инциденты по системе «Сбои Ядра».

- `id` — UUID, первичный ключ.
- `user_id` — UUID, not null, ссылка на `users.id` с каскадным удалением.
- `lesson_id` — UUID, ссылка на `lessons.id`.
- `level` — VARCHAR(10), not null. Возможные значения: 'glitch', 'failure', 'crash'.
- `description` — TEXT, not null (описание ошибки).
- `resolved` — BOOLEAN, not null, default FALSE.
- `resolved_at` — TIMESTAMPTZ.
- `created_at` — TIMESTAMPTZ, not null, default NOW().

Индексы: по `user_id`, по `level`, по `resolved`.

---

## 💰 ПЛАТЕЖИ — transactions

Хранит информацию о платежах и подписках.

- `id` — UUID, первичный ключ.
- `user_id` — UUID, not null, ссылка на `users.id`.
- `amount` — INTEGER, not null (в копейках).
- `currency` — VARCHAR(3), not null, default 'RUB'.
- `type` — VARCHAR(20), not null. Возможные значения: 'course_purchase', 'subscription', 'coins_pack'.
- `status` — VARCHAR(20), not null, default 'pending'. Возможные значения: 'pending', 'completed', 'failed', 'refunded'.
- `external_id` — VARCHAR(255) (ID транзакции в платёжной системе).
- `created_at` — TIMESTAMPTZ, not null, default NOW().

Индексы: по `user_id`, по `status`, по `external_id`.

---

## 🛒 МАГАЗИН — shop_items, user_inventory

**shop_items:**

- `id` — UUID, первичный ключ.
- `name` — VARCHAR(100), not null.
- `description` — TEXT.
- `item_type` — VARCHAR(20), not null. Возможные значения: 'avatar_part', 'badge_slot', 'termix_skin', 'power_up'.
- `price_coins` — INTEGER, not null.
- `image_url` — VARCHAR(500).
- `required_rank` — VARCHAR(20).
- `is_limited` — BOOLEAN, not null, default FALSE.
- `created_at` — TIMESTAMPTZ, not null, default NOW().

**user_inventory:**

- `user_id` — UUID, not null, ссылка на `users.id` с каскадным удалением.
- `item_id` — UUID, not null, ссылка на `shop_items.id` с каскадным удалением.
- `purchased_at` — TIMESTAMPTZ, not null, default NOW().
- `is_active` — BOOLEAN, not null, default FALSE.

Первичный ключ: (`user_id`, `item_id`).

---

## 🔐 API КЛЮЧИ — api_keys

Хранит API-ключи для внешних интеграций.

- `id` — UUID, первичный ключ.
- `user_id` — UUID, not null, ссылка на `users.id` с каскадным удалением.
- `key_hash` — VARCHAR(255), not null.
- `name` — VARCHAR(100), not null.
- `permissions` — JSONB, not null, default '["read"]'.
- `last_used_at` — TIMESTAMPTZ.
- `expires_at` — TIMESTAMPTZ.
- `is_active` — BOOLEAN, not null, default TRUE.
- `created_at` — TIMESTAMPTZ, not null, default NOW().

Индексы: по `user_id`.

---

## 🐱 ФРАЗА-СХЕМА

> «База данных Termix Academy — это трюм пиратского корабля.
>
> Всё разложено по сундукам.
> Пользователи — в одном. Курсы — в другом. Баджи — в третьем.
>
> И каждая таблица знает своё место.
> Порядок в трюме — порядок в плавании.»
>
> **— Termix, кибер-пиратский кот, Хранитель Ядра**