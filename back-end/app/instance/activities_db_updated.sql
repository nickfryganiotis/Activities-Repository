CREATE TABLE `activity` (
  `id` int PRIMARY KEY,
  `created_at` datetime DEFAULT (now()),
  `min_age` int,
  `max_age` int,
  `periodicity` varchar(255),
  `duration` int,
  `presence` varchar(255),
  `subgrouping` int,
  `teacher_role` varchar(255),
  `source` varchar(255),
  `source_type` varchar(255),
  `apriory` int,
  `posteriory` int
);

CREATE TABLE `activity_translation` (
  `id` int PRIMARY KEY,
  `activity_id` int,
  `language_code` varchar(255),
  `title` varchar(255),
  `learning_objectives` varchar(255),
  `description` varchar(255),
  `evaluation` varchar(255),
  `material` varchar(255)
);

CREATE TABLE `didactic_strategy` (
  `id` int PRIMARY KEY,
  `code` varchar(255)
);

CREATE TABLE `activity_didactic_strategy` (
  `id` int PRIMARY KEY,
  `activity_id` int,
  `strategy_id` int
);

CREATE TABLE `competence` (
  `id` int PRIMARY KEY,
  `code` varchar(255)
);

CREATE TABLE `activity_competence` (
  `id` int PRIMARY KEY,
  `activity_id` int,
  `competence_id` int
);

CREATE TABLE `special_need` (
  `id` int PRIMARY KEY,
  `code` varchar(255)
);

CREATE TABLE `activity_special_need` (
  `id` int PRIMARY KEY,
  `activity_id` int,
  `special_need_id` int
);

ALTER TABLE `activity` ADD FOREIGN KEY (`apriory`) REFERENCES `activity` (`id`);

ALTER TABLE `activity` ADD FOREIGN KEY (`posteriory`) REFERENCES `activity` (`id`);

ALTER TABLE `activity_translation` ADD FOREIGN KEY (`activity_id`) REFERENCES `activity` (`id`);

ALTER TABLE `activity_didactic_strategy` ADD FOREIGN KEY (`activity_id`) REFERENCES `activity` (`id`);

ALTER TABLE `activity_didactic_strategy` ADD FOREIGN KEY (`strategy_id`) REFERENCES `didactic_strategy` (`id`);

ALTER TABLE `activity_competence` ADD FOREIGN KEY (`activity_id`) REFERENCES `activity` (`id`);

ALTER TABLE `activity_competence` ADD FOREIGN KEY (`competence_id`) REFERENCES `competence` (`id`);

ALTER TABLE `activity_special_need` ADD FOREIGN KEY (`activity_id`) REFERENCES `activity` (`id`);

ALTER TABLE `activity_special_need` ADD FOREIGN KEY (`special_need_id`) REFERENCES `special_need` (`id`);
