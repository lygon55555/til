# RxSwift
> RxSwift를 공부하고 정리한 내용입니다.

## 목차
|#|제목|내용|
|:---:|:---|:---|
|00|👋 [RxSwift](https://github.com/lygon55555/TIL/blob/main/RxSwift/00.%20RxSwift.md)|RxSwift란?|
|01|🔭 [Observables and Observers](https://github.com/lygon55555/TIL/blob/main/RxSwift/01.%20Observables%20and%20Observers.md)|Observable 생성, 구독, Observer|
|02|🧹 [Disposables](https://github.com/lygon55555/til/blob/main/RxSwift/02.%20Disposables.md)|Disposables, 리소스 해제, 실행 취소|
|03|➕ [Operators](https://github.com/lygon55555/til/blob/main/RxSwift/03.%20Operators.md)|연산자(Operators)|
|04|📖 [Subject](https://github.com/lygon55555/til/blob/main/RxSwift/04.%20Subject.md)|`Subject` : PublishSubject, BehaviorSubject, ReplaySubject, AsyncSubject <br/> `Relay` : PublishRelay, BehaviorRelay|
|05|✏️ [Create Operators](https://github.com/lygon55555/til/blob/main/RxSwift/05.%20Create%20Operators.md)|Observable을 생성하는 연산자<br/>`just`, `of`, `from`, `range`, `generate`<br/>`repeatElement`, `deferred`, `create`, `empty`, `error`|
|06|🧫 [Filtering Operators](https://github.com/lygon55555/til/blob/main/RxSwift/06.%20Filtering%20Operators.md)|소스 Observable로부터 요소를 선택적으로 방출하는 연산자<br/>`ignoreElements`, `elementAt`, `filter`<br/>`skip`, `skipWhile`, `skipUntil`<br/>`take`, `takeWhile`, `takeUntil`, `takeLast`<br/>`single`, `distinctUntilChanged`, `debounce`, `throttle`|
|07|💱 [Transforming Operators](https://github.com/lygon55555/til/blob/main/RxSwift/07.%20Transforming%20Operators.md)|Observable에 의해 방출된 요소들을 변형하는 연산자<br/>`toArray`, `map`<br/>`flatMap`, `flatMapFirst`, `flatMapLatest`<br/>`scan`, `buffer`, `window`, `groupBy`|
|08|🎒 [Combining Operators](https://github.com/lygon55555/til/blob/main/RxSwift/08.%20Combining%20Operators.md)|다수의 소스 Observable을 작업하여 하나의 Observable을 생성하는 연산자<br/>`startWith`, `concat`, `merge`, `combineLatest`, `zip`<br/>`withLatestFrom`, `sample`, `switchLatest`, `reduce`|
|09|☑️ [Conditional Operators](https://github.com/lygon55555/til/blob/main/RxSwift/09.%20Conditional%20Operators.md)|하나 이상의 Observable 또는 Observable이 배출한 항목을 평가하는 연산자<br/>`amb`|
|10|⏲️ [Time-based Operators](https://github.com/lygon55555/til/blob/main/RxSwift/10.%20Time-based%20Operators.md)|시간 기반의 연산자<br/>`interval`, `timer`, `timeout`, `delay`, `delaySubscription`|
|11|🌐 Sharing Subscription||  
|12|📅 Scheduler||  
|13|⚠️ Warning||  