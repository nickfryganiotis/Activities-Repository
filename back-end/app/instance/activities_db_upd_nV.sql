CREATE TABLE `activity` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL,
  `min_age` int DEFAULT NULL,
  `max_age` int DEFAULT NULL,
  `periodicity` varchar(255) DEFAULT NULL,
  `duration` int DEFAULT NULL,
  `presence` varchar(255) DEFAULT NULL,
  `sub_grouping` int DEFAULT NULL,
  `teacher_role` varchar(255) DEFAULT NULL,
  `source` varchar(255) DEFAULT NULL,
  `source_type` varchar(255) DEFAULT NULL,
  `apriory` int DEFAULT NULL,
  `posteriory` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `apriory` (`apriory`),
  KEY `posteriory` (`posteriory`),
  CONSTRAINT `activity_ibfk_1` FOREIGN KEY (`apriory`) REFERENCES `activity` (`id`),
  CONSTRAINT `activity_ibfk_2` FOREIGN KEY (`posteriory`) REFERENCES `activity` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `activity_competence` (
  `id` int NOT NULL AUTO_INCREMENT,
  `activity_id` int DEFAULT NULL,
  `competence_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `activity_id` (`activity_id`),
  KEY `competence_id` (`competence_id`),
  CONSTRAINT `activity_competence_ibfk_1` FOREIGN KEY (`activity_id`) REFERENCES `activity` (`id`),
  CONSTRAINT `activity_competence_ibfk_2` FOREIGN KEY (`competence_id`) REFERENCES `competence` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `activity_didactic_strategy` (
  `id` int NOT NULL AUTO_INCREMENT,
  `activity_id` int DEFAULT NULL,
  `strategy_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `activity_id` (`activity_id`),
  KEY `strategy_id` (`strategy_id`),
  CONSTRAINT `activity_didactic_strategy_ibfk_1` FOREIGN KEY (`activity_id`) REFERENCES `activity` (`id`),
  CONSTRAINT `activity_didactic_strategy_ibfk_2` FOREIGN KEY (`strategy_id`) REFERENCES `didactic_strategy` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `activity_special_need` (
  `id` int NOT NULL AUTO_INCREMENT,
  `activity_id` int DEFAULT NULL,
  `special_need_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `activity_id` (`activity_id`),
  KEY `special_need_id` (`special_need_id`),
  CONSTRAINT `activity_special_need_ibfk_1` FOREIGN KEY (`activity_id`) REFERENCES `activity` (`id`),
  CONSTRAINT `activity_special_need_ibfk_2` FOREIGN KEY (`special_need_id`) REFERENCES `special_need` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `activity_translation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `activity_id` int DEFAULT NULL,
  `language_code` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `learning_objectives` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `evaluation` varchar(255) DEFAULT NULL,
  `material` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT `activity_translation_ibfk_1` FOREIGN KEY (`activity_id`) REFERENCES `activity` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `competence` (
  `id` int NOT NULL AUTO_INCREMENT,
  `code` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `didactic_strategy` (
  `id` int NOT NULL AUTO_INCREMENT,
  `code` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `special_need` (
  `id` int NOT NULL AUTO_INCREMENT,
  `code` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;