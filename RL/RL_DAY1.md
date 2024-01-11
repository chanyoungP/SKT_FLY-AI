# Reinforcement Learning 

## 0. Introduction of RL 

### 1. Categories of Machine Learning
- Supervised Learning (fully labeled)
- Semi-Supervised Learning (Partially labeled)
    - RL is here 
- Un-Supervised Learning 

### 2. RL Algorithms
- Model-free 
- Model-based 

### 3. Key point of RL 
- State 
- Actions
- Rewards 
    - Start with index 2 

### 4. Environments
- Fully observable Environments
    - like board game 
    - Markov Decision Process (MDP) known
- Partially observable Environments
    - Unknown MDP 

### 5. Components of an RL Agent
- Policy
    - compute next action of Agent
- Value function
    - compute how is good for long-term about action or state
- Model 

### 6. Gradient Descent
- weight - gradient of objective function 

## 1. Markov Decision Process (MDP)

### 1. Markov Process
- MDP for RL 
> 환경을 완전히 관찰할 수 있다는 가정이 필요 <br>
거의 모든 퍼즐 문제들은 MDP를 사용하여 모델링 가능

- Episodes
> Agent가 환경하고 액션을 주고 받으면서 환경에서 수집되는 데이터 <br>

- Transition matrix 
> 에이전트가 환경과 상호 작용하는 과정에서 상태(State) 간의 전이(Transition) 확률을 기록한 행렬입니다.

### 2. Markov Reward Process (State(S) , Transition Matrix(P), Rewards(R))
- Reward 
> 어떤 상태에서의 Expected Reward는 현재 state에서 어떤 액션을 취했을 때, 다음 state에서의 Reward 평균

- Return $$ G_t $$ 
> 시간 단계 t부터 미래까지의 보상의 총합  <br>
time step t+1부터 t+i까지의 Reward 총합 

- Bellman Equation 
$$
v(s_i) = r(s_i) + \gamma\sum{p_{ij}R_j}
$$


### Markov Decision Process
- (SAPR)
> S : finite state <br>
> A : Action <br>
> P : Transition Prob <br>
> 

- Bellman Equation 
$$ V(s) = R(s) + \gamma \cdot \max_a \sum_{s'} P(s' | s, a) \cdot V(s') 
$$

- solve bellman eq -> update policy 


State (S):

Represents the current situation or configuration of the agent in the environment.
Action (A):

Denotes the action taken by the agent in the current state.
Reward (R):

Represents the immediate reward received by the agent for taking the action in the current state.
Next State (S'):

Represents the state that the environment transitions to after the agent takes the action in the current state.
Next Action (A'):

Denotes the next action that the agent will take in the next state.

