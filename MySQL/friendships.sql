INSERT into users ( first_name, last_name, created_at, updated_at) 
VALUES ("Martin", "Velasque", NOW(), NOW()), ("Zoel","Nguyen", NOW(), NOW()), ("Justin", "Tong", NOW(), NOW()), ("Kevin", "Choi", NOW(), NOW()),
("Shahan", "Vahid", NOW(), NOW()), ("Timothy", "Ben", NOW(), NOW()), ("Patrick", "Tamaya", NOW(), NOW());

INSERT into friendships (user_id, friend_id, created_at, updated_at)
VALUES (1,2,NOW(), NOW()), (1,4,NOW(), NOW()), (2,4,NOW(), NOW()),(2,5,NOW(), NOW()),(7,6,NOW(), NOW()), (1,6,NOW(), NOW()), (3,5,NOW(), NOW());

SELECT users.first_name as first_name, users.last_name as last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name  
FROM users 
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as user2 ON user2.id = friendships.friend_id;

