CREATE TABLE `activity` (
  `id` int NOT NULL AUTO_INCREMENT,
  `activity_title` varchar(100) NOT NULL,
  `learning_objectives` varchar(500) DEFAULT NULL,
  `description` text,
  `target_age_group_left` int DEFAULT NULL,
  `target_age_group_right` int DEFAULT NULL,
  `periodicity` int DEFAULT NULL,
  `duration` int DEFAULT NULL,
  `presence` varchar(100) DEFAULT NULL,
  `sub_grouping` varchar(100) DEFAULT NULL,
  `teacher_role` varchar(100) DEFAULT NULL,
  `evaluation` text,
  `material_description` text,
  `img_url` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `adapted_to_special_needs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `special_need_title` varchar(100) NOT NULL,
  `activity_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT `adapted_to_special_needs_ibfk_1` FOREIGN KEY (`activity_id`) REFERENCES `activity` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `didactic_strategies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `didactic_strategy_title` varchar(100) NOT NULL,
  `activity_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT `didactic_strategies_ibfk_1` FOREIGN KEY (`activity_id`) REFERENCES `activity` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `emo_socio_competencies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `emosocio_competency_title` varchar(100) NOT NULL,
  `activity_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT `emo_socio_competencies_ibfk_1` FOREIGN KEY (`activity_id`) REFERENCES `activity` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `language` (
  `id` int NOT NULL AUTO_INCREMENT,
  `language_title` varchar(100) NOT NULL,
  `activity_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT `language_ibfk_1` FOREIGN KEY (`activity_id`) REFERENCES `activity` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `publications` (
  `id` int NOT NULL AUTO_INCREMENT,
  `publication_title` varchar(100) NOT NULL,
  `activity_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT `publications_ibfk_1` FOREIGN KEY (`activity_id`) REFERENCES `activity` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;