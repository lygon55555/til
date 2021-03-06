# CHAPTER 00 – 오리엔테이션

- 코드의 진행을 멈출 수 있는 특정한 표시를 코드 내 원하는 위치에 삽입할 수 있는데, 이를 브레이크 포인트(Breakpoints, 중단점)이라고 함
- 클래스 파일 등의 텍스트 기반 파일을 편집할 때에는 일반 에디터가 실행되며, 스토리보드 파일이나 nib, xib 파일을 편집할 때에는 인터페이스 빌더가 실행됨
- 디버그 내비게이터에서는 모든 함수 호출 경로를 역순으로 표시해줌 → 함수의 호출 스택(Stack)
- CPU와 메모리, 디스크 사용량이나 네트워크 사용량의 경우 해당 항목을 클릭하여 상세 정보를 확인할 수 있음. 특히 이들 정보 제공 화면의 UI는 매우 유려하기 때문에 모니터에 켜 놓는 것만으로도 주변 사람들에게 일한다는 느낌을 주는 부수적인 효과도 있음
- 이 기능을 이용하면 특정 시점에서 네트워크 사용량이라든가 메모리 사용량, CPU 이용률 등을 모두 체크할 수 있으므로, 앱을 모두 개발하고 난 후 성능 개선 작업을 한다던가 메모리 누수 현상을 잡는 데에 중점적으로 활용됨
- 실행이 중단되었을 때, 브레이크 포인트가 걸린 해당 라인과 그 이하의 라인들은 모두 아직 실행되기 전이다
- 디버그 영역에 위치한 세 번째 아이콘을 클릭하면 현재 단계의 브레이크 포인트를 넘어 다음 브레이크 포인트까지 코드가 진행됨
- ‘뷰 계층 디버거(View Hierarchy)’라고 불리는 도구를 통해, 런타임 환경에서 뷰 계층의 구조를 살펴보고, 사용자 인터페이스를 디버깅할 수 있다.
- 태그(Tag)는 브랜치와 유사하지만 특정 시점에서의 소스 코드를 그대로 보관하며 최초 생성 이후로 변경이나 수정이 반영되지 않는 특성을 가짐
- 생성된 태그는 보관 자체에 목적이 있는 경우도 있지만, 새로운 브랜치를 만드는 바탕으로 사용되기도 함.
- 예를 들어, 앱을 만들어 앱스토어에 배포한 후 2차 개발이 진행되던 도중에 갑자기 2차 개발과는 무관한 새로운 기능 업데이트가 필요한 상황이라면 이때 배포 시점에 만들어 둔 태그를 이용하여 새로운 브랜치를 만들고 여기에서 기능 업데이트를 진행하는 식으로 간단히 처리할 수 있음
- 태그나 브랜치는 항상 프로젝트 전체를 대상으로만 생성할 수 있음
