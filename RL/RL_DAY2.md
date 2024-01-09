# Reinfocement learning _day2

## TD learning 

### what is TD learning
- Temporal-Difference learning
> TD 학습의 주된 목표는 각 상태의 가치를 추정하는 것입니다. 이를 통해 에이전트는 환경과의 상호 작용을 통해 기대되는 미래 보상을 예측할 수 있습니다. <br>
보통의 강화학습 문제에서는 각 state에서의 가치를 알기가 어렵기 때문에 추정하는 것? 

- TD Error=Reward+γ⋅Estimated Value of Next State−Estimated Value of Current State 
$$
TD Error = Reward + \gamma EstimatedValue_{t+1} - Estimated Value_t
$$

### MC vs TD
- 학습 시점
> MC 학습: 에피소드가 끝난 후에만 업데이트가 이루어집니다. 에피소드는 에이전트가 시작 상태에서 목표 상태에 도달할 때까지의 상호 작용을 나타남 <br>
TD 학습: 각 타임 스텝에서 업데이트가 이루어집니다. 에피소드의 각 단계에서 TD 오차를 사용하여 가치 함수를 업데이트

- 방법론
> MC 학습: 실제 반환(실제로 경험한 보상의 총합)과 예측 반환(현재 추정된 가치 함수에 기반한 반환) 간의 차이를 최소화하는 방향으로 학습 <br>
TD 학습: TD 오차(현재 추정된 가치와 다음 상태의 추정 가치의 차이)를 사용하여 가치 함수를 업데이트

- 상호작용
> MC 학습: 에이전트가 완전한 에피소드를 경험한 후에 가치를 업데이트 <br>
TD 학습: 각 타임 스텝에서 에이전트가 현재 상태에서 받은 보상과 다음 상태의 추정 가치를 사용하여 가치를 업데이트

### On-policy vs Off-policy
- On-policy (온-폴리시):
> On-policy 학습에서는 에이전트가 현재 사용하는 정책(policy)에 대한 경험을 기반으로 학습합니다.

> 주로 TD(시간 차이) 학습과 같은 방법들이 On-policy로 간주됩니다.


>예를 들어, SARSA(상태-행동-보상-다음상태-다음행동) 알고리즘은 On-policy 학습의 한 예입니다.


- Off-policy (오프-폴리시):

> Off-policy 학습에서는 에이전트가 사용하는 정책과는 독립적으로 다른 정책에서 얻은 데이터를 사용하여 학습합니다.

>주로 Q-learning과 같은 방법들이 Off-policy로 간주됩니다.

> 예를 들어, Q-learning 알고리즘은 에이전트가 현재 사용 중인 정책이 아닌, 예를 들어 입실론-그리디 정책으로 수집한 데이터를 사용하여 가치 함수를 업데이트합니다.