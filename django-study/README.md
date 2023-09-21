# django-study
* Do it! 파이썬 웹 개발의 정석(2021) 예제 프로젝트 clone

---

### 사용해보니...

#### Spring과 비교했을 때 장점
* 꽤 완성도 있는 Admin 페이지 제공
* 특별한 설정을 거치지 않아도 기본적으로 제공해주는 기능이 많다

#### Spring과 비교했을 때 단점
* 비즈니스 로직을 어디로 분리해둬야 하는지 잘 모르겠다


---
### 현 예제 프로젝트의 문제점
* Query가 최적화되어 있지 않아서 쿼리가 다량 발생. 장고도 마찬가지로 쿼리 최적화는 별도로 진행해야 하는 것으로 추정됨. 추가적인 스터디가 필요함
* (0.001) SELECT COUNT(*) AS "__count" FROM "blog_post" WHERE "blog_post"."category_id" IS NULL; args=(); alias=default   
  (0.000) SELECT 1 AS "a" FROM "blog_post" LIMIT 1; args=(1,); alias=default   
  (0.000) SELECT "blog_post"."id", "blog_post"."thumbnail", "blog_post"."file", "blog_post"."title", "blog_post"."content", "blog_post"."hook_text", "blog_post"."author_id", "blog_post"."category_id", "blog_post"."created_at", "blog_post"."updated_at" FROM "blog_post" ORDER BY "blog_post"."created_at" DESC; args=(); alias=default   
  (0.000) SELECT 1 AS "a" FROM "blog_tag" INNER JOIN "blog_post_tags" ON ("blog_tag"."id" = "blog_post_tags"."tag_id") WHERE "blog_post_tags"."post_id" = 14 LIMIT 1; args=(1, 14); alias=default   
  (0.000) SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 1 LIMIT 21; args=(1,); alias=default   
  (0.000) SELECT "blog_category"."id", "blog_category"."name", "blog_category"."slug" FROM "blog_category" WHERE "blog_category"."id" = 1 LIMIT 21; args=(1,); alias=default   
  (0.000) SELECT 1 AS "a" FROM "blog_tag" INNER JOIN "blog_post_tags" ON ("blog_tag"."id" = "blog_post_tags"."tag_id") WHERE "blog_post_tags"."post_id" = 13 LIMIT 1; args=(1, 13); alias=default   
  (0.000) SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 1 LIMIT 21; args=(1,); alias=default   
  (0.000) SELECT "blog_category"."id", "blog_category"."name", "blog_category"."slug" FROM "blog_category" WHERE "blog_category"."id" = 1 LIMIT 21; args=(1,); alias=default   
  (0.000) SELECT 1 AS "a" FROM "blog_tag" INNER JOIN "blog_post_tags" ON ("blog_tag"."id" = "blog_post_tags"."tag_id") WHERE "blog_post_tags"."post_id" = 12 LIMIT 1; args=(1, 12); alias=default   
  (0.000) SELECT "blog_tag"."id", "blog_tag"."name", "blog_tag"."slug" FROM "blog_tag" INNER JOIN "blog_post_tags" ON ("blog_tag"."id" = "blog_post_tags"."tag_id") WHERE "blog_post_tags"."post_id" = 12; args=(12,); alias=default   
   ...이하 생략