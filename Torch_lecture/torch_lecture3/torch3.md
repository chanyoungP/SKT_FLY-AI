# 자연어 처리 

## Attention 

### self-attention 
The animal didn't cross the street because it was too tired 

it을 번역하려면 스스로 분석을 통해 가능한 경우에 대해서 attention을 걸어줘야한다. 


### Transformer

- Encoder 
> 숫자화 시키는 행위 
>
> input  seq -> Encoder -> latent seq 
- Decoder 
> latent seq -> Decoder -> output seq 
>
> Transformer 는 encoder 부분에 self attention을 도입하여 input 자체의 의미를 파악하고 그 의미를 디코더로 보내서 원하는 output으로 바꾼다. 
>
> Positional encoding 정보를 같이 넣어준다. 
>

> 쿼리 키 벨류 
> 쿼리 : 문장 입력 단어들 
> 키 , 벨류 : 번역할 단어들 
>
> 나는 너를 매우 사랑해
> i love you so much 
>
> 나는 -> embedding vector 와 가장 유사한 key vector 를 찾아서 두 벡터를 곱한다. -> 유사도 계산(코사인) -> embedding 값 자체를 중요도로 생각하고 곱해준다. 
> 즉, Attention = 쿼리 * 키 *값(embedding 값) Q K 내적으로 단어간 유사성을 구하고 V를 곱해서 중요하고 관련있는 단어에 더 관심을 둔다. 
> QK = cosine(Q,K) 크기가 1이라서 식이 성립 
> SOFTMAX(QK) -> 유사성을 확률로 나타냄 . 
>
> 
### Attention(Q,K,V) = softmax(QK)V :: attention score를 나타내는 벡터 

### Multi-Head Attention : 여러 관점에서 attention을 달리준다. 
해석의 다양성을 중시한다. 
                                            
