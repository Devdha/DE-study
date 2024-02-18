## Week1

### Assignments

[x] fastAPI로 root에 접속 시 `Hello, World!` 를 반환하는 초간단 서버를 만듭니다.

- [main.py](./main.py)

[x] 초간단 서버를 Dockerfile로 컨테이너화합니다.

- [Dockerfile](./Dockerfile)

[x] EC2(t2.micro)를 만들고 도커로 띄웁니다. 외부에서 접속이 되는지 확인합니다.

- 완료
  - 생각보다 신경 써줘야 할 것이 많다.
  - 기본 유저는 ec2-user이다. 해당 유저로 연결을 시도하니 연결이 된다.
  - apt-get이 아닌 yum을 사용했다.
  - `docker run -p 80:80`으로 포트를 안 열어줘서 처음엔 동작안함
- EC2 상에서 docker run
- Postman으로 연결 확인

[x] ECS fargate로 서버를 띄웁니다. 외부에서 접속이 되는지 확인합니다.

- ECR 권한이 없어서, 포기할까 하다가 docker hub에 있는 [fastapi-hello-world 이미지](https://hub.docker.com/r/asdkant/fastapi-hello-world) 사용
- Postman으로 연결 확인

[x] 로드밸런서는 쓰지 않습니다.

[x] 구현 및 배포 디테일을 리드미에 정리해주세요. 기타 배운 개념들을 정리하셔도 좋습니다.
