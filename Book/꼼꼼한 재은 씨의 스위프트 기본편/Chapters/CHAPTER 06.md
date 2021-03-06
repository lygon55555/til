# CHAPTER 06 - 사용자에게 메시지를 전달하는 방법

- 로컬, 노티피케이션, 푸시 노티피케이션 (로컬 푸시, 서버 푸시)
- 로컬 푸시가 앱 내부에서 특정 프로세스에 의해 등록된 메시지를 iOS가 전달하는 방식이라면 서버 푸시는 별도의 서버를 통해 APNs(Apple Push Notification Service)라는 애플 고유의 메시징 시스템에게 보낸 메시지가 네트워크를 통해 전달되는 방식임

# 6.1 메시지 알림창 – UIAlertController

- UIAlertControllersms 크게 두 가지 형태의 메시지 창을 표현할 수 있음
    - 알림창 – 모달(Modal) 방식 O
    - 액션 시트 – 모달 방식 X
- 모달이란 창이 닫힐 때까지 그 창을 제외한 화면의 다른 부분은 반응할 수 없도록 잠기는 것을 말함. 알림창이 표시되는 동안 사용자가 터치할 수 있는 곳은 오로지 알림창의 선택 버튼뿐이다.
- 액션 시트는 메시지가 떠 있는 동안에도 메시지 창이 아닌 다른 영역을 건드릴 수 있으며, 그 결과로 액션 시트 창이 닫힘.
- UIAlertController는 비동기(Asynchronize) 방식으로 실행돼서 애플리케이션 자체적으로 실행하는 내용이 있다면 알림창이 표시되고 있더라도 계속 실행됨
- 기존의 실행 흐름을 방해하지 않는 선에서 새로운 실행 흐름을 만들어 내는 것을 비동기 방식이라고 함

## 6.1.1 UIAlertController

- UIAlertController가 메시지 창 그 자체를 담당한다면, UIAlertAction은 메시지 창에 들어갈 버튼을 구현하는 객체이다.
- 메시지 창을 구현하기 위해 가장 먼저 해야 할 일은 UIAlertController 클래스의 인스턴스를 생성하는 것. 이때 모두 세 개의 인자값이 사용되는데, 각각 메시지 창의 타이틀, 메시지 내용, 그리고 메시지 창의 스타일 값을 결정함
- 세 번째 매개변수로 정의된 preferredStyle은 알림창과 액션 시트를 결정하는 값임
- 열거형 타입으로 변수나 상수가 이미 정의되어 있다면, 값을 대입할 때 열거형 객체의 이름을 생략하고 값만 선택해서 입력할 수 있음
    - 축약되지 않은 형태 – preferredStyle: UIAlertController.Style.alert
    - 축약된 형태 – preferredStyle: .alert
- 메시지 창에서 버튼은 모두 하나의 액션으로 취급되는데, 이는 각각의 버튼마다 동작을 가지기 때문
- 버튼 타입 값으로 .cancel을 사용하면 아무것도 실행되지 않은 채 메시지 창의 액션이 취소된다는 것을 뜻하며, 메시지 창 내에서는 한 번만 사용할 수 있음
- .destructive는 주로 중요한 내용을 변경하거나 삭제해서 되돌릴 수 없는 결정을 하는 버튼에 적용되며, 이 타입이 적용된 버튼은 빨간색으로 강조됨.
- 일반적인 버튼은 모두 .default 타입으로 선택하면 됨
- UIAlertAction 클래스 초기화 구문에서 사용되는 세 번째 매개변수는 버튼을 클릭했을 때 실행될 구문이고 함수나 클로저 형태로 작성됨
- 세 번째 매개변수에 사용되는 함수 또는 클로저는 UIAlertAction 타입의 인자값 하나를 입력받는 형식으로 정의되어 있어야 함. 하지만 클로저를 통해 처리할 내용이 아무 것도 없다면 클로저의 매개변수는 언더바로 대신할 수 있음
- 트레일링 클로저 문법도 적용할 수 있음
- UIAlertController는 또 다른 하나의 화면이라 생각하고 프레젠트 메소드를 이용하여 화면을 전환시켜 줘야 하고 버튼이 클릭되면 창은 자동으로 닫히기 때문에 dismiss(animated:) 메소드를 구현해 줄 필요는 없음
- UIAlertController에 여러 개의 버튼을 추가했을 경우 보통은 추가하는 순서대로 버튼이 나열되지만 .cancel로 설정된 객체는 항상 메시지 창의 맨 아래에 위치하는 특성을 가짐
- 액션 시트에서도 .cancel 타입으로 설정된 버튼은 화면 제일 아래에 분리되어 표시됨
- 화면이 뜨자마자 자동으로 메시지 창을 띄워주어야 할 때가 있음. 네트워크 기반 서비스에서 네트워크가 연결되지 않았을 때가 대표적인 경우.
    - viewDidLoad() 메소드 내에서 메시지 창을 구현하여 실행하면 런타임 오류가 발생 → 아직 메시지 창을 처리해 줄 뷰가 화면에 구현되지 않은 상태에서 먼저 화면 전환을 시도했기 때문
    - viewDidAppear(_:) 메소드를 이용하여 메시지 창을 처리 → 뷰 객체가 메모리에만 올라온 상태에서 호출되는 viewDidLoad(_:) 메소드와 달리 viewDidAppear(_:) 메소드는 뷰가 완전히 화면에 표현되고 난 다음에 호출되기 때문

## 6.1.2 입력 필트를 가지는 메시지 창

- UIAlertController 객체에 텍스트 필드를 추가
    - addTextField(configurationHandler:) 메소드를 호출
    - 인자값으로 클로저가 사용되는데, 이 클로저의 목적은 추가된 텍스트 필드의 속성을 설정하는 것
    - 따라서 클로저가 직접 참조할 수 있도록 텍스트 필드 객체 정보가 클로저의 인자값으로 전달됨
    - placeholder 속성은 텍스트 필드에 값이 비어 있을 때 안내 메시지 역할을 하고, isSecureTextEntry 속성은 비밀번호 입력 필드처럼 입력된 값을 ***로 처리하는 역할을 함
- 메시지 창에 추가할 수 있는 텍스트 필드의 수는 여러 개이기 때문에 textFields 속성의 타입 역시 배열로 이루어짐. 첫 번째 텍스트 필드를 참조하려면 인덱스 0번을 통해 배열의 첫 번째 인자를 읽어 들여야 함 → 배열의 첫 번째 인자만을 가리키는 속성인 .first를 이용
- 메시지 창에 추가된 텍스트 필드가 2개 이상이면 그에 맞는 인덱스 번호를 사용하여 textFields 배열에서 알맞은 값을 읽어낼 수 있음
- 클로저의 다양한 표현 형식
    
    ```swift
    // [원형]
    alert.addTextField(configurationHandler: { (textField: UITextField) in
    	textField.placeholder = "비밀번호"
    	textField.isSecureTextEntry = true
    }
    
    // [변형1] 클로저 인자값 대신 메소드에 실행 블록 추가
    alert.addTextField() { (textField: UITextField) in
    	textField.placeholder = "비밀번호"
    	textField.isSecureTextEntry = true
    }
    
    // [변형2] 클로저 인자값의 타입 생략
    alert.addTextField() { (tf) in
    	tf.placeholder = "비밀번호"
    	tf.isSecureTextEntry = true
    }
    
    // [변형3] 클로저 인자값을 생략
    alert.addTextField() { 
    	$0.placeholder = "비밀번호"
    	$0.isSecureTextEntry = true
    }
    ```
    

# 6.2 로컬 알림

- 로컬 알림은 앱 내부에서 만든 특정 메시지를 iOS의 알림 센터를 통해 전달하는 방법임
- 로컬 알림은 iOS 스케줄러에 의해 발송되는데, 앱 내부에서 미리 메시지를 구성한 후 발송될 시각을 iOS 스케줄러에 등록해 두면 해당 시각에 맞추어 자동으로 발송됨

## 6.2.1 UserNotification 프레임워크를 이용한 로컬 알림

- UserNotification은 사용자 알림을 처리하기 위해 iOS 10부터 새롭게 도입된 알림 전용 프레임워크 → UN 접두어를 사용하여 객체 이름을 정의
- UNMutableNotificationContent는 알림에 필요한 메시지와 같은 기본적인 속성을 담는 알림 콘텐츠 역할을 함. 이 객체를 통해 로컬 알림 타이틀, 서브 타이틀 및 알림 메시지를 설정할 수 있으며 앱 아이콘에 표시될 배지나 사운드 설정도 모두 이 객체를 통해 설정함
- UNTimeIntervalNotificationTrigger는 알림 발송 조건을 관리함. 설정할 수 있는 속성은 발생 시각과 반복 여부.
- UNMutableNotificationContent와 UNTimeIntervalNotificationTrigger를 통해 알림 콘텐츠와 알림 발생 조건이 준비되면 이들을 모아 알림 요청 객체를 만들어야 함. 이때 사용되는 클래스가 UNNotificationRequest이다. 알림 콘텐츠 객체와 알림 발송 조건 객체를 인자값으로 하여 이 클래스를 초기화하면 그 결과로 알림 요청 객체가 생성됨.
- UNUserNotificationCenter는 실제 발송을 담당하는 센터임. 등록된 알림 내용을 확인하고 정해진 시각에 발송하는 역할을 맡음. 이 객체는 싱글턴 방식으로 동작하기 때문에 따로 인스턴스를 생성하지 않고 current() 메소드를 통해 참조 정보만 가져올 수 있음. 앞에서 생성한 UNNotificationRequest 객체를 UNNotificationCenter::add(_:) 메소드를 이용하여 추가하기만 하면 알림 등록 과정이 모두 완료됨

## 6.2.2 기본 실습

- Application(_:didFinishLaunchingWithOptions:) 메소드는 앱이 처음 실행될 때 호출되는 메소드로 애플리케이션에서 사용할 클래스와 리소스들이 모두 메모리에 로드되고 아직 애플리케이션의 첫 화면을 모바일 디바이스에 띄우기 직전, 그러니까 시작 화면이 스크린에 표시되고 있는 동안 호출됨
- UserNotification 프레임워크에서는 로컬 알림 또는 푸시 알림을 사용하기 위해 UNUserNotificationCenter 객체를 이용하여 미리 알림 설정 환경을 정의하고, 이 설정 내용을 사용자에게 승인받는 과정을 거쳐야 함.
    - UNUserNotificationCenter는 싱글톤 패턴으로 정의되어 있어서 current()를 통해 시스템에서 제공하는 인스턴스를 받아올 수 있음
    - 인스턴스를 받아왔다면, requestAuthorization() 메소드를 호출하여 사용자에게 알림 설정에 대한 동의를 받아야 함.
    - 첫 번째 인자값은 알림 메시지에 포함될 항목들이고 여러 항목을 한꺼번에 입력할 수 있도록 배열 타입으로 정의되어 있음
    - 두 번째 인자값은 클로저이다. 사용자가 메시지 창의 버튼을 눌렀을 때 실행되며 알림 동의 여부를 true / false 형태로 전달받는 첫 번째 매개변수와 오류 발생시 사용하는 오류 객체 타입의 두 번째 매개변수로 이루어짐.
    - applicationWillResignActive(_:) 메소드는 앱이 활성화 상태를 잃었을 때 실행되는 메소드임
- 알림 메시지를 보내기 위해 먼저 확인해야 하는 것은 사용자의 동의 여부이다.
- 사용자가 Allow 또는 허용 버튼을 클릭했다면 getNotificationSettings() 메소드의 인자값 클로저에 전달되는 settings 객체에서 .authorizationStatus 속성값은 authorized로 설정됨.
- 로컬 알림은 발송할 내용을 정의하는 1단계, 발송 조건을 정의하는 2단계, 알림 요청을 만드는 3단계를 거쳐 노티피케이션 센터에 해당 요청을 등록하는 4단계까지 차례로 연결됨
- 1단계에서 가장 먼저 해야 할 것은 발송할 내용을 정의하기 위한 UNMutableNotificationContent 객체를 생성하는 것임
- .badge 속성은 앱 아이콘에 표시될 값임
- Title 속성과 subtitle 속성은 각각 알림창에 표시될 메시지의 제목과 소제목을 나타냄
- body에는 우리가 전달하고 싶은 내용을 넣을 수 있으며, 긴 문장도 전달 가능
- .sound 속성을 통해 우리는 알림이 도착했을 때 알려줄 사운드를 설정할 수 있음
- userInfo는 로컬 알림과 함께 전달하고 싶은 값이 있을 때 사용하는 속성이다. 딕셔너리 타입의 이 속성에 저장된 값은 화면에는 표시되지 않지만 이 알림을 눌러서 연결되는 앱 델리게이트 메소드에서는 참조할 수 있음
- 알림 발송 시간을 설정할 수 있도록 두 가지 객체를 제공
    - UNTimeIntervalNotificationTrigger : 발송 시각과 반복 여부를 설정할 수 있고 입력값의 단위는 초이다.
    - 하루 중 특정 시각을 지정하여 알림 메시지를 전송할 때에는 UNCalendarNotificationTrigger 객체가 사용됨.
- 설정한 발송 내용과 발송 조건들은 알림 요청 객체의 일부분으로 포함되어 UNNotificationRequest 객체로 만들어지고 첫 번째 인자값인 identifier는 해당 알림에 대한 임의의 식별 아이디, 두 번째 인자값인 content는 발송할 내용, 세 번째 인자값인 trigger에는 발송 시각 조건을 넣어주면 됨. 식별 아이디는 주로 이미 등록된 알림 요청을 취소하고 싶을 때 여러 개의 알림 요청들 중에서 원하는 것을 식별하는 용도로 많이 사용됨
- 발송할 메시지 내용과 발송 조건을 담아 생성한 알림 요청 객체를 노티피케이션 센터에 추가하고 나면 끝이다. 노티피케이션 센터는 등록된 알림 내용을 iOS의 스케줄링 센터에 등록하고, 정해진 시간에 발송되도록 처리해줌.

## 6.2.3 받은 알림 처리하기

- UserNotification 프레임워크에서는 ‘델리게이트 패턴’이라고 불리는 프로그래밍 구조를 사용하여 요구사항을 처리할 수 있도록 지원함
- 앱이 실행되는 도중에 알림 메시지가 도착할 경우 userNotificationCenter(_:willPresent:withCompletionHandler:) 메소드가 자동으로 호출됨. 알림 배너의 표시 여부와 상관없이 이 메소드가 호출됨.
- 사용자가 알림 메시지를 실제로 클릭하면 userNotificationCenter(_:didReceive:withCompletionHandler:) 메소드가 자동으로 호출됨. 알림 메시지에 대한 정보는 모두 위 메소드의 두 번째 인자값인 response 매개변수에 담겨 전달됨.
- request.identifier는 로컬 알림 등록시 입력한 식별 아이디를 읽어오는 속성이며, notification.request.content.userInfo 속성은 사용자가 커스텀으로 정의한 정보를 읽어오는 역할을 함.

6.2.6 미리 알림 기능 구현

- main.async {…}는 백그라운드에서 실행되는 로직을 메인 쓰레드에서 실행되도록 처리해주는 역할을 함. iOS 프로그램 실행 영역은 UI 등의 주요 처리를 담당하는 메인 실행 영역과 그리 중요하지 않은 처리를 담당하는 백그라운드 실행 영역으로 나누어지는데, 대부분의 비동기 클로저 구문은 백그라운드 실행 영역에서 처리됨. UI 처리는 모두 메인 실행 영역에서 이루어져야됨. 메인 실행 영역에서 처리되어야 하는 부분을 해당 구문으로 감싸주면, 그 범위의 코드는 모두 메인 실행 영역에서 수행됨.
