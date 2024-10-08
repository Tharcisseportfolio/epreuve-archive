-- PRAGMA foreign_keys=OFF;
-- BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY SERIAL, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO django_migrations VALUES(1,'contenttypes','0001_initial','2024-08-03 11:41:28.334734');
INSERT INTO django_migrations VALUES(2,'auth','0001_initial','2024-08-03 11:41:28.339895');
INSERT INTO django_migrations VALUES(3,'admin','0001_initial','2024-08-03 11:41:28.347772');
INSERT INTO django_migrations VALUES(4,'admin','0002_logentry_remove_auto_add','2024-08-03 11:41:28.352070');
INSERT INTO django_migrations VALUES(5,'admin','0003_logentry_add_action_flag_choices','2024-08-03 11:41:28.354535');
INSERT INTO django_migrations VALUES(6,'api','0001_initial','2024-08-03 11:41:28.361523');
INSERT INTO django_migrations VALUES(7,'api','0002_alter_contactmessage_table_alter_sendemail_table','2024-08-03 11:41:28.362798');
INSERT INTO django_migrations VALUES(8,'api','0003_alter_contactmessage_table_alter_sendemail_table','2024-08-03 11:41:28.364049');
INSERT INTO django_migrations VALUES(9,'contenttypes','0002_remove_content_type_name','2024-08-03 11:41:28.373152');
INSERT INTO django_migrations VALUES(10,'auth','0002_alter_permission_name_max_length','2024-08-03 11:41:28.377884');
INSERT INTO django_migrations VALUES(11,'auth','0003_alter_user_email_max_length','2024-08-03 11:41:28.382481');
INSERT INTO django_migrations VALUES(12,'auth','0004_alter_user_username_opts','2024-08-03 11:41:28.385522');
INSERT INTO django_migrations VALUES(13,'auth','0005_alter_user_last_login_null','2024-08-03 11:41:28.389718');
INSERT INTO django_migrations VALUES(14,'auth','0006_require_contenttypes_0002','2024-08-03 11:41:28.390272');
INSERT INTO django_migrations VALUES(15,'auth','0007_alter_validators_add_error_messages','2024-08-03 11:41:28.393431');
INSERT INTO django_migrations VALUES(16,'auth','0008_alter_user_username_max_length','2024-08-03 11:41:28.397525');
INSERT INTO django_migrations VALUES(17,'auth','0009_alter_user_last_name_max_length','2024-08-03 11:41:28.401216');
INSERT INTO django_migrations VALUES(18,'auth','0010_alter_group_name_max_length','2024-08-03 11:41:28.405142');
INSERT INTO django_migrations VALUES(19,'auth','0011_update_proxy_permissions','2024-08-03 11:41:28.410197');
INSERT INTO django_migrations VALUES(20,'auth','0012_alter_user_first_name_max_length','2024-08-03 11:41:28.413773');
INSERT INTO django_migrations VALUES(21,'sessions','0001_initial','2024-08-03 11:41:28.414966');
INSERT INTO django_migrations VALUES(22,'tests','0001_initial','2024-08-03 11:41:28.418650');
INSERT INTO django_migrations VALUES(23,'tests','0002_alter_course_section_alter_test_section','2024-08-03 11:41:28.423784');
INSERT INTO django_migrations VALUES(24,'tests','0003_grade_alter_test_course_course_grade','2024-08-03 11:41:28.429976');
INSERT INTO django_migrations VALUES(25,'tests','0004_test_type_alter_test_link','2024-08-03 11:41:28.435815');
INSERT INTO django_migrations VALUES(26,'token_blacklist','0001_initial','2024-08-03 11:41:28.443275');
INSERT INTO django_migrations VALUES(27,'token_blacklist','0002_outstandingtoken_jti_hex','2024-08-03 11:41:28.447098');
INSERT INTO django_migrations VALUES(28,'token_blacklist','0003_auto_20171017_2007','2024-08-03 11:41:28.453245');
INSERT INTO django_migrations VALUES(29,'token_blacklist','0004_auto_20171017_2013','2024-08-03 11:41:28.458609');
INSERT INTO django_migrations VALUES(30,'token_blacklist','0005_remove_outstandingtoken_jti','2024-08-03 11:41:28.463530');
INSERT INTO django_migrations VALUES(31,'token_blacklist','0006_auto_20171017_2113','2024-08-03 11:41:28.467815');
INSERT INTO django_migrations VALUES(32,'token_blacklist','0007_auto_20171017_2214','2024-08-03 11:41:28.478104');
INSERT INTO django_migrations VALUES(33,'token_blacklist','0008_migrate_to_bigautofield','2024-08-03 11:41:28.486197');
INSERT INTO django_migrations VALUES(34,'token_blacklist','0010_fix_migrate_to_bigautofield','2024-08-03 11:41:28.493364');
INSERT INTO django_migrations VALUES(35,'token_blacklist','0011_linearizes_history','2024-08-03 11:41:28.494360');
INSERT INTO django_migrations VALUES(36,'token_blacklist','0012_alter_outstandingtoken_user','2024-08-03 11:41:28.497159');
CREATE TABLE IF NOT EXISTS "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY SERIAL, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY SERIAL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY SERIAL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO auth_user_user_permissions VALUES(1,2,1);
INSERT INTO auth_user_user_permissions VALUES(2,2,2);
INSERT INTO auth_user_user_permissions VALUES(3,2,3);
INSERT INTO auth_user_user_permissions VALUES(4,2,4);
INSERT INTO auth_user_user_permissions VALUES(5,2,5);
INSERT INTO auth_user_user_permissions VALUES(6,2,6);
INSERT INTO auth_user_user_permissions VALUES(7,2,7);
INSERT INTO auth_user_user_permissions VALUES(8,2,8);
INSERT INTO auth_user_user_permissions VALUES(9,2,9);
INSERT INTO auth_user_user_permissions VALUES(10,2,10);
INSERT INTO auth_user_user_permissions VALUES(11,2,11);
INSERT INTO auth_user_user_permissions VALUES(12,2,12);
INSERT INTO auth_user_user_permissions VALUES(13,2,13);
INSERT INTO auth_user_user_permissions VALUES(14,2,14);
INSERT INTO auth_user_user_permissions VALUES(15,2,15);
INSERT INTO auth_user_user_permissions VALUES(16,2,16);
INSERT INTO auth_user_user_permissions VALUES(17,2,17);
INSERT INTO auth_user_user_permissions VALUES(18,2,18);
INSERT INTO auth_user_user_permissions VALUES(19,2,19);
INSERT INTO auth_user_user_permissions VALUES(20,2,20);
INSERT INTO auth_user_user_permissions VALUES(21,2,21);
INSERT INTO auth_user_user_permissions VALUES(22,2,22);
INSERT INTO auth_user_user_permissions VALUES(23,2,23);
INSERT INTO auth_user_user_permissions VALUES(24,2,24);
INSERT INTO auth_user_user_permissions VALUES(25,2,25);
INSERT INTO auth_user_user_permissions VALUES(26,2,26);
INSERT INTO auth_user_user_permissions VALUES(27,2,27);
INSERT INTO auth_user_user_permissions VALUES(28,2,28);
INSERT INTO auth_user_user_permissions VALUES(29,2,29);
INSERT INTO auth_user_user_permissions VALUES(30,2,30);
INSERT INTO auth_user_user_permissions VALUES(31,2,31);
INSERT INTO auth_user_user_permissions VALUES(32,2,32);
INSERT INTO auth_user_user_permissions VALUES(33,2,33);
INSERT INTO auth_user_user_permissions VALUES(34,2,34);
INSERT INTO auth_user_user_permissions VALUES(35,2,35);
INSERT INTO auth_user_user_permissions VALUES(36,2,36);
INSERT INTO auth_user_user_permissions VALUES(37,2,37);
INSERT INTO auth_user_user_permissions VALUES(38,2,38);
INSERT INTO auth_user_user_permissions VALUES(39,2,39);
INSERT INTO auth_user_user_permissions VALUES(40,2,40);
INSERT INTO auth_user_user_permissions VALUES(41,2,41);
INSERT INTO auth_user_user_permissions VALUES(42,2,42);
INSERT INTO auth_user_user_permissions VALUES(43,2,43);
INSERT INTO auth_user_user_permissions VALUES(44,2,44);
INSERT INTO auth_user_user_permissions VALUES(45,2,45);
INSERT INTO auth_user_user_permissions VALUES(46,2,46);
INSERT INTO auth_user_user_permissions VALUES(47,2,47);
INSERT INTO auth_user_user_permissions VALUES(48,2,48);
INSERT INTO auth_user_user_permissions VALUES(49,2,49);
INSERT INTO auth_user_user_permissions VALUES(50,2,50);
INSERT INTO auth_user_user_permissions VALUES(51,2,51);
INSERT INTO auth_user_user_permissions VALUES(52,2,52);
INSERT INTO auth_user_user_permissions VALUES(53,2,53);
INSERT INTO auth_user_user_permissions VALUES(54,2,54);
INSERT INTO auth_user_user_permissions VALUES(55,2,55);
INSERT INTO auth_user_user_permissions VALUES(56,2,56);
INSERT INTO auth_user_user_permissions VALUES(57,2,57);
INSERT INTO auth_user_user_permissions VALUES(58,2,58);
INSERT INTO auth_user_user_permissions VALUES(59,2,59);
INSERT INTO auth_user_user_permissions VALUES(60,2,60);
INSERT INTO auth_user_user_permissions VALUES(61,2,61);
INSERT INTO auth_user_user_permissions VALUES(62,2,62);
INSERT INTO auth_user_user_permissions VALUES(63,2,63);
INSERT INTO auth_user_user_permissions VALUES(64,2,64);
INSERT INTO auth_user_user_permissions VALUES(65,2,65);
INSERT INTO auth_user_user_permissions VALUES(66,2,66);
INSERT INTO auth_user_user_permissions VALUES(67,2,67);
INSERT INTO auth_user_user_permissions VALUES(68,2,68);
INSERT INTO auth_user_user_permissions VALUES(69,2,69);
INSERT INTO auth_user_user_permissions VALUES(70,2,70);
INSERT INTO auth_user_user_permissions VALUES(71,2,71);
INSERT INTO auth_user_user_permissions VALUES(72,2,72);
CREATE TABLE IF NOT EXISTS "django_admin_log" ("id" integer NOT NULL PRIMARY KEY SERIAL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);
INSERT INTO django_admin_log VALUES(1,'1','3',1,'[{"added": {}}]',10,1,'2024-08-03 11:42:57.002882');
INSERT INTO django_admin_log VALUES(2,'2','9',1,'[{"added": {}}]',10,1,'2024-08-03 11:43:01.000057');
INSERT INTO django_admin_log VALUES(3,'1','Langues',1,'[{"added": {}}]',11,1,'2024-08-03 11:43:32.879640');
INSERT INTO django_admin_log VALUES(4,'1','Anglais',1,'[{"added": {}}]',13,1,'2024-08-03 11:43:34.930798');
INSERT INTO django_admin_log VALUES(5,'2','Francais',1,'[{"added": {}}]',13,1,'2024-08-03 11:43:51.638314');
INSERT INTO django_admin_log VALUES(6,'2','Math & Physique',1,'[{"added": {}}]',11,1,'2024-08-03 11:44:04.217212');
INSERT INTO django_admin_log VALUES(7,'3','Informatique de Gestion',1,'[{"added": {}}]',11,1,'2024-08-03 11:44:16.276903');
INSERT INTO django_admin_log VALUES(8,'4','Bio & Chimie',1,'[{"added": {}}]',11,1,'2024-08-03 11:44:28.271850');
INSERT INTO django_admin_log VALUES(9,'5','Science Sociale',1,'[{"added": {}}]',11,1,'2024-08-03 11:44:40.672132');
INSERT INTO django_admin_log VALUES(10,'6','Pédagogies',1,'[{"added": {}}]',11,1,'2024-08-03 11:44:49.048472');
INSERT INTO django_admin_log VALUES(11,'7','Statistique',1,'[{"added": {}}]',11,1,'2024-08-03 11:44:59.553422');
INSERT INTO django_admin_log VALUES(12,'3','Mathematique',1,'[{"added": {}}]',13,1,'2024-08-03 11:45:41.747928');
INSERT INTO django_admin_log VALUES(13,'4','Chimie',1,'[{"added": {}}]',13,1,'2024-08-03 11:45:56.703225');
INSERT INTO django_admin_log VALUES(14,'5','science humaines',1,'[{"added": {}}]',13,1,'2024-08-03 11:46:09.602343');
INSERT INTO django_admin_log VALUES(15,'6','Enseignement stratégique',1,'[{"added": {}}]',13,1,'2024-08-03 11:46:38.396314');
INSERT INTO django_admin_log VALUES(16,'3','Mathematique',2,'[{"changed": {"fields": ["Grade"]}}]',13,1,'2024-08-03 11:47:02.527865');
INSERT INTO django_admin_log VALUES(17,'8','Pas de section parce que c''est 9ème',1,'[{"added": {}}]',11,1,'2024-08-03 11:47:38.847983');
INSERT INTO django_admin_log VALUES(18,'7','Mathematic',1,'[{"added": {}}]',13,1,'2024-08-03 11:47:48.743658');
INSERT INTO django_admin_log VALUES(19,'8','Science et technologies',1,'[{"added": {}}]',13,1,'2024-08-03 11:48:10.008112');
INSERT INTO django_admin_log VALUES(20,'8','Science et technologies',2,'[{"changed": {"fields": ["Grade"]}}]',13,1,'2024-08-03 11:48:21.074768');
INSERT INTO django_admin_log VALUES(21,'1','Epreuve d''anglais Serie A',1,'[{"added": {}}]',14,1,'2024-08-03 11:49:32.196361');
INSERT INTO django_admin_log VALUES(22,'2','Epreuve de français série B',1,'[{"added": {}}]',14,1,'2024-08-03 11:50:12.806531');
INSERT INTO django_admin_log VALUES(23,'3','Epreuve de mathematique inventaire',1,'[{"added": {}}]',14,1,'2024-08-03 11:50:53.011589');
INSERT INTO django_admin_log VALUES(24,'4','Epreuve de pedagogies',1,'[{"added": {}}]',14,1,'2024-08-03 11:51:19.979508');
INSERT INTO django_admin_log VALUES(25,'2','tharcisse',1,'[{"added": {}}]',4,1,'2024-08-03 11:52:45.813884');
INSERT INTO django_admin_log VALUES(26,'2','tharcisse',2,'[{"changed": {"fields": ["First name", "Last name", "Email address", "Staff status", "Superuser status", "User permissions", "Last login"]}}]',4,1,'2024-08-03 11:53:29.514126');
INSERT INTO django_admin_log VALUES(27,'5','Epreuve d''anglais',1,'[{"added": {}}]',14,1,'2024-08-06 17:10:20.496736');
CREATE TABLE IF NOT EXISTS "api_contactmessage" ("id" integer NOT NULL PRIMARY KEY SERIAL, "subject" varchar(100) NOT NULL, "email" varchar(254) NOT NULL, "message" text NOT NULL, "received_at" datetime NOT NULL);
INSERT INTO api_contactmessage VALUES(1,'Trying to send a feedback','tharcissentira@gmail.com','I am sending you the email so that u love what u like','2024-08-03 19:59:58.854084');
CREATE TABLE IF NOT EXISTS "api_grade" ("id" integer NOT NULL PRIMARY KEY SERIAL, "grade" varchar(40) NULL);
INSERT INTO api_grade VALUES(1,'3');
INSERT INTO api_grade VALUES(2,'9');
CREATE TABLE IF NOT EXISTS "api_section" ("id" integer NOT NULL PRIMARY KEY SERIAL, "section" varchar(100) NOT NULL);
INSERT INTO api_section VALUES(1,'Langues');
INSERT INTO api_section VALUES(2,'Math & Physique');
INSERT INTO api_section VALUES(3,'Informatique de Gestion');
INSERT INTO api_section VALUES(4,'Bio & Chimie');
INSERT INTO api_section VALUES(5,'Science Sociale');
INSERT INTO api_section VALUES(6,'Pédagogies');
INSERT INTO api_section VALUES(7,'Statistique');
INSERT INTO api_section VALUES(8,'Pas de section parce que c''est 9ème');
CREATE TABLE IF NOT EXISTS "api_sendemail" ("id" integer NOT NULL PRIMARY KEY SERIAL, "subject" varchar(100) NOT NULL, "message" text NOT NULL, "email" varchar(254) NOT NULL, "sent_at" datetime NOT NULL);
INSERT INTO api_sendemail VALUES(1,'Sending love','I am sending love so that you feel okay for using our website','tharcissentira@gmail.com','2024-08-03 19:23:15.563626');
INSERT INTO api_sendemail VALUES(2,'Sending love','I am sending love so that you feel okay for using our website','tharcissentira@gmail.com','2024-08-03 19:24:12.006411');
INSERT INTO api_sendemail VALUES(3,'Sending love','Burundi is the love','tharcissentira@gmail.com','2024-08-03 19:54:27.130873');
INSERT INTO api_sendemail VALUES(4,'Sending Love','I love this things','tharcissentira@gmail.com','2024-08-03 19:57:43.067324');
CREATE TABLE IF NOT EXISTS "api_course" ("id" integer NOT NULL PRIMARY KEY SERIAL, "course" varchar(100) NOT NULL, "grade_id" bigint NULL REFERENCES "api_grade" ("id") DEFERRABLE INITIALLY DEFERRED, "section_id" bigint NOT NULL REFERENCES "api_section" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO api_course VALUES(1,'Anglais',1,1);
INSERT INTO api_course VALUES(2,'Francais',1,1);
INSERT INTO api_course VALUES(3,'Mathematique',1,2);
INSERT INTO api_course VALUES(4,'Chimie',1,4);
INSERT INTO api_course VALUES(5,'science humaines',1,5);
INSERT INTO api_course VALUES(6,'Enseignement stratégique',1,6);
INSERT INTO api_course VALUES(7,'Mathematic',2,8);
INSERT INTO api_course VALUES(8,'Science et technologies',2,8);
CREATE TABLE IF NOT EXISTS "api_test" ("id" integer NOT NULL PRIMARY KEY SERIAL, "test" varchar(100) NOT NULL, "link" varchar(100) NOT NULL, "type" varchar(1) NOT NULL, "year" date NOT NULL, "course_id" bigint NULL REFERENCES "api_course" ("id") DEFERRABLE INITIALLY DEFERRED, "section_id" bigint NOT NULL REFERENCES "api_section" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO api_test VALUES(1,'Epreuve d''anglais Serie A','documents/COHORT9-Electronic-version-2-1_mBhNtSz.pdf','Q','2024-03-12',1,1);
INSERT INTO api_test VALUES(2,'Epreuve de français série B','documents/cropped-visa_1_2.jpeg','Q','2024-08-02',2,1);
INSERT INTO api_test VALUES(3,'Epreuve de mathematique inventaire','documents/cropped-visa_1_2_WtJRz95.jpeg','A','2023-07-10',3,2);
INSERT INTO api_test VALUES(4,'Epreuve de pedagogies','documents/cropped-visa_1_2_Lr2PFEx.jpeg','Q','2024-08-01',6,6);
INSERT INTO api_test VALUES(5,'Epreuve d''anglais','documents/IMIGWI_YINTAMBO_IJANYE_NMATORA.pdf','Q','2024-08-06',1,1);
CREATE TABLE IF NOT EXISTS "django_content_type" ("id" integer NOT NULL PRIMARY KEY SERIAL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO django_content_type VALUES(1,'admin','logentry');
INSERT INTO django_content_type VALUES(2,'auth','permission');
INSERT INTO django_content_type VALUES(3,'auth','group');
INSERT INTO django_content_type VALUES(4,'auth','user');
INSERT INTO django_content_type VALUES(5,'contenttypes','contenttype');
INSERT INTO django_content_type VALUES(6,'sessions','session');
INSERT INTO django_content_type VALUES(7,'token_blacklist','blacklistedtoken');
INSERT INTO django_content_type VALUES(8,'token_blacklist','outstandingtoken');
INSERT INTO django_content_type VALUES(9,'api','contactmessage');
INSERT INTO django_content_type VALUES(10,'api','grade');
INSERT INTO django_content_type VALUES(11,'api','section');
INSERT INTO django_content_type VALUES(12,'api','sendemail');
INSERT INTO django_content_type VALUES(13,'api','course');
INSERT INTO django_content_type VALUES(14,'api','test');
INSERT INTO django_content_type VALUES(15,'tests','section');
INSERT INTO django_content_type VALUES(16,'tests','course');
INSERT INTO django_content_type VALUES(17,'tests','test');
INSERT INTO django_content_type VALUES(18,'tests','grade');
CREATE TABLE IF NOT EXISTS "auth_permission" ("id" integer NOT NULL PRIMARY KEY SERIAL, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO auth_permission VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO auth_permission VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO auth_permission VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO auth_permission VALUES(4,1,'view_logentry','Can view log entry');
INSERT INTO auth_permission VALUES(5,2,'add_permission','Can add permission');
INSERT INTO auth_permission VALUES(6,2,'change_permission','Can change permission');
INSERT INTO auth_permission VALUES(7,2,'delete_permission','Can delete permission');
INSERT INTO auth_permission VALUES(8,2,'view_permission','Can view permission');
INSERT INTO auth_permission VALUES(9,3,'add_group','Can add group');
INSERT INTO auth_permission VALUES(10,3,'change_group','Can change group');
INSERT INTO auth_permission VALUES(11,3,'delete_group','Can delete group');
INSERT INTO auth_permission VALUES(12,3,'view_group','Can view group');
INSERT INTO auth_permission VALUES(13,4,'add_user','Can add user');
INSERT INTO auth_permission VALUES(14,4,'change_user','Can change user');
INSERT INTO auth_permission VALUES(15,4,'delete_user','Can delete user');
INSERT INTO auth_permission VALUES(16,4,'view_user','Can view user');
INSERT INTO auth_permission VALUES(17,5,'add_contenttype','Can add content type');
INSERT INTO auth_permission VALUES(18,5,'change_contenttype','Can change content type');
INSERT INTO auth_permission VALUES(19,5,'delete_contenttype','Can delete content type');
INSERT INTO auth_permission VALUES(20,5,'view_contenttype','Can view content type');
INSERT INTO auth_permission VALUES(21,6,'add_session','Can add session');
INSERT INTO auth_permission VALUES(22,6,'change_session','Can change session');
INSERT INTO auth_permission VALUES(23,6,'delete_session','Can delete session');
INSERT INTO auth_permission VALUES(24,6,'view_session','Can view session');
INSERT INTO auth_permission VALUES(25,7,'add_blacklistedtoken','Can add blacklisted token');
INSERT INTO auth_permission VALUES(26,7,'change_blacklistedtoken','Can change blacklisted token');
INSERT INTO auth_permission VALUES(27,7,'delete_blacklistedtoken','Can delete blacklisted token');
INSERT INTO auth_permission VALUES(28,7,'view_blacklistedtoken','Can view blacklisted token');
INSERT INTO auth_permission VALUES(29,8,'add_outstandingtoken','Can add outstanding token');
INSERT INTO auth_permission VALUES(30,8,'change_outstandingtoken','Can change outstanding token');
INSERT INTO auth_permission VALUES(31,8,'delete_outstandingtoken','Can delete outstanding token');
INSERT INTO auth_permission VALUES(32,8,'view_outstandingtoken','Can view outstanding token');
INSERT INTO auth_permission VALUES(33,9,'add_contactmessage','Can add contact message');
INSERT INTO auth_permission VALUES(34,9,'change_contactmessage','Can change contact message');
INSERT INTO auth_permission VALUES(35,9,'delete_contactmessage','Can delete contact message');
INSERT INTO auth_permission VALUES(36,9,'view_contactmessage','Can view contact message');
INSERT INTO auth_permission VALUES(37,10,'add_grade','Can add grade');
INSERT INTO auth_permission VALUES(38,10,'change_grade','Can change grade');
INSERT INTO auth_permission VALUES(39,10,'delete_grade','Can delete grade');
INSERT INTO auth_permission VALUES(40,10,'view_grade','Can view grade');
INSERT INTO auth_permission VALUES(41,11,'add_section','Can add section');
INSERT INTO auth_permission VALUES(42,11,'change_section','Can change section');
INSERT INTO auth_permission VALUES(43,11,'delete_section','Can delete section');
INSERT INTO auth_permission VALUES(44,11,'view_section','Can view section');
INSERT INTO auth_permission VALUES(45,12,'add_sendemail','Can add send email');
INSERT INTO auth_permission VALUES(46,12,'change_sendemail','Can change send email');
INSERT INTO auth_permission VALUES(47,12,'delete_sendemail','Can delete send email');
INSERT INTO auth_permission VALUES(48,12,'view_sendemail','Can view send email');
INSERT INTO auth_permission VALUES(49,13,'add_course','Can add course');
INSERT INTO auth_permission VALUES(50,13,'change_course','Can change course');
INSERT INTO auth_permission VALUES(51,13,'delete_course','Can delete course');
INSERT INTO auth_permission VALUES(52,13,'view_course','Can view course');
INSERT INTO auth_permission VALUES(53,14,'add_test','Can add test');
INSERT INTO auth_permission VALUES(54,14,'change_test','Can change test');
INSERT INTO auth_permission VALUES(55,14,'delete_test','Can delete test');
INSERT INTO auth_permission VALUES(56,14,'view_test','Can view test');
INSERT INTO auth_permission VALUES(57,15,'add_section','Can add section');
INSERT INTO auth_permission VALUES(58,15,'change_section','Can change section');
INSERT INTO auth_permission VALUES(59,15,'delete_section','Can delete section');
INSERT INTO auth_permission VALUES(60,15,'view_section','Can view section');
INSERT INTO auth_permission VALUES(61,16,'add_course','Can add course');
INSERT INTO auth_permission VALUES(62,16,'change_course','Can change course');
INSERT INTO auth_permission VALUES(63,16,'delete_course','Can delete course');
INSERT INTO auth_permission VALUES(64,16,'view_course','Can view course');
INSERT INTO auth_permission VALUES(65,17,'add_test','Can add test');
INSERT INTO auth_permission VALUES(66,17,'change_test','Can change test');
INSERT INTO auth_permission VALUES(67,17,'delete_test','Can delete test');
INSERT INTO auth_permission VALUES(68,17,'view_test','Can view test');
INSERT INTO auth_permission VALUES(69,18,'add_grade','Can add grade');
INSERT INTO auth_permission VALUES(70,18,'change_grade','Can change grade');
INSERT INTO auth_permission VALUES(71,18,'delete_grade','Can delete grade');
INSERT INTO auth_permission VALUES(72,18,'view_grade','Can view grade');
CREATE TABLE IF NOT EXISTS "auth_group" ("id" integer NOT NULL PRIMARY KEY SERIAL, "name" varchar(150) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "auth_user" ("id" integer NOT NULL PRIMARY KEY SERIAL, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "first_name" varchar(150) NOT NULL);
INSERT INTO auth_user VALUES(1,'pbkdf2_sha256$720000$fmySRdueKRupr8vhe7fSYd$613kb77c7fURpIUDeZmUAawQf1y3/QhikKipC3LA7hE=','2024-08-05 16:23:09.115532',1,'tk','','',1,1,'2024-08-03 11:42:34.147280','');
INSERT INTO auth_user VALUES(2,'pbkdf2_sha256$720000$dkDjeKfATR0T4gePfVkX0h$wWnI2Y250MJpHELtdsdb7A1/n4b/3hCf3KZPnrq0SkQ=','2024-08-05 12:00:00',1,'tharcisse','ntirandekura','tntirand@oberlin.edu',1,1,'2024-08-03 11:52:45','Tharcisse');
CREATE TABLE IF NOT EXISTS "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO django_session VALUES('eqsmedyt6w3huclxnj0m89nj2jlyz7gt','.eJxVjM0OwiAQhN-FsyEtsPx49O4zkGVZpWogKe3J-O62SQ96mmS-b-YtIq5LiWvnOU5ZnMUoTr9dQnpy3UF-YL03Sa0u85TkrsiDdnltmV-Xw_07KNjLttYIbAM4xRbT4Axav6VXoJWFwJkoOE6QR7yhHtCz9kTKGh2SB49GfL7fEjfZ:1sb0UH:JgAhSVoP2eqN1QWcbpi6B-CP0R22w4aolryVj9hzzJU','2024-08-19 16:23:09.116582');
CREATE TABLE IF NOT EXISTS "tests_section" ("id" integer NOT NULL PRIMARY KEY SERIAL, "section" varchar(100) NOT NULL);
CREATE TABLE IF NOT EXISTS "tests_course" ("id" integer NOT NULL PRIMARY KEY SERIAL, "course" varchar(100) NOT NULL, "code" varchar(10) NOT NULL, "section_id" bigint NOT NULL REFERENCES "tests_section" ("id") DEFERRABLE INITIALLY DEFERRED, "grade_id" bigint NULL REFERENCES "tests_grade" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "tests_grade" ("id" integer NOT NULL PRIMARY KEY SERIAL, "grade" varchar(40) NULL);
CREATE TABLE IF NOT EXISTS "tests_test" ("id" integer NOT NULL PRIMARY KEY SERIAL, "test" varchar(100) NOT NULL, "year" date NOT NULL, "course_id" bigint NULL REFERENCES "tests_course" ("id") DEFERRABLE INITIALLY DEFERRED, "section_id" bigint NOT NULL REFERENCES "tests_section" ("id") DEFERRABLE INITIALLY DEFERRED, "type" varchar(1) NOT NULL, "link" varchar(100) NOT NULL);
CREATE TABLE IF NOT EXISTS "token_blacklist_blacklistedtoken" ("blacklisted_at" datetime NOT NULL, "token_id" bigint NOT NULL UNIQUE REFERENCES "token_blacklist_outstandingtoken" ("id") DEFERRABLE INITIALLY DEFERRED, "id" integer NOT NULL PRIMARY KEY SERIAL);
CREATE TABLE IF NOT EXISTS "token_blacklist_outstandingtoken" ("token" text NOT NULL, "created_at" datetime NULL, "expires_at" datetime NOT NULL, "user_id" integer NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "jti" varchar(255) NOT NULL UNIQUE, "id" integer NOT NULL PRIMARY KEY SERIAL);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('django_migrations',36);
INSERT INTO sqlite_sequence VALUES('django_admin_log',27);
INSERT INTO sqlite_sequence VALUES('django_content_type',18);
INSERT INTO sqlite_sequence VALUES('auth_permission',72);
INSERT INTO sqlite_sequence VALUES('auth_group',0);
INSERT INTO sqlite_sequence VALUES('auth_user',2);
INSERT INTO sqlite_sequence VALUES('tests_course',0);
INSERT INTO sqlite_sequence VALUES('tests_test',0);
INSERT INTO sqlite_sequence VALUES('token_blacklist_blacklistedtoken',0);
INSERT INTO sqlite_sequence VALUES('token_blacklist_outstandingtoken',0);
INSERT INTO sqlite_sequence VALUES('api_grade',2);
INSERT INTO sqlite_sequence VALUES('api_section',8);
INSERT INTO sqlite_sequence VALUES('api_course',8);
INSERT INTO sqlite_sequence VALUES('api_test',5);
INSERT INTO sqlite_sequence VALUES('auth_user_user_permissions',72);
INSERT INTO sqlite_sequence VALUES('api_sendemail',4);
INSERT INTO sqlite_sequence VALUES('api_contactmessage',1);
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE INDEX "api_course_grade_id_a204389b" ON "api_course" ("grade_id");
CREATE INDEX "api_course_section_id_c3c27796" ON "api_course" ("section_id");
CREATE INDEX "api_test_course_id_b27fe471" ON "api_test" ("course_id");
CREATE INDEX "api_test_section_id_df8c4a08" ON "api_test" ("section_id");
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE INDEX "tests_course_section_id_09908fe7" ON "tests_course" ("section_id");
CREATE INDEX "tests_course_grade_id_0df5c776" ON "tests_course" ("grade_id");
CREATE INDEX "tests_test_course_id_b185464b" ON "tests_test" ("course_id");
CREATE INDEX "tests_test_section_id_087388c8" ON "tests_test" ("section_id");
CREATE INDEX "token_blacklist_outstandingtoken_user_id_83bc629a" ON "token_blacklist_outstandingtoken" ("user_id");
-- COMMIT;
