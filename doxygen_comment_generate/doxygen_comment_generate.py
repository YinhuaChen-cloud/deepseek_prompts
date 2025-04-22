from openai import OpenAI
import os

# 根据环境变量获取 openai key\n",
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')

client = OpenAI(
    base_url="https://api.deepseek.com/",
    api_key=deepseek_api_key
)

instructions = """
作为资深代码文档专家，你擅长分析各种编程语言的函数并生成专业级Doxygen注释。请遵循以下规则：

以下是你要生成的注释风格：
/** 
 * 简要描述(以动词开头，如"Calculates...")
 * 
 * 详细描述函数功能、算法(如使用)、边界条件和重要实现细节。
 * 对于复杂函数，可以分段描述。
 * @param <name> <parameter description>(注明类型和约束)
 * @return <return value description>(注明类型和可能取值)
 * @throw <exception> <circumstances>(如适用)
 * @note <any notable aspects>(如线程安全、性能等)
 * @warning <any potential pitfalls>(如内存管理、副作用等)
 */

下面是一个例子：
你接收到了一个C语言输入：
```c
long long dot(int *x, int *y, int n) \{
    long long product = 0;
    for(int i = 0; i < n; i++)
        product += x[i] * y[i];
    return product;
\}
```

你要输出：
```
/**
* 计算两个整数数组的点积
* 对两个长度相同的整数数组执行点积运算。通过累加对应元素乘积的方式计算结果。*
* 函数假设输入数组至少有n个有效元素，调用者需保证这一点。
* @param x 指向第一个整数数组的指针(int*类型)
* @param y 指向第二个整数数组的指针(int*类型)
* @param n 数组的长度/要计算的元素数量(int类型)
* @return 64位点积累加结果(long long类型)
* @warning 不检查空指针或数组越界情况
* @note 时间复杂度O(n)
* @note 对于大数组(n>10^6)，考虑使用并行化优化
*/
```

现在请为以下函数生成完整Doxygen注释，注意，仅生成注释即可，不要附加任何其它东西！
"""

prompt = """
```c
int max(int *x, int n) {
    int maxnum = 0;
    for(int i = 0; i < n; i++) {
        if(maxnum < x[i])
            maxnum = x[i];
    }
    return maxnum;
}
```
"""

completion = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "system",
            "content": instructions
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=1.3,
    stream=False,
    # max_tokens=2048, 
)

print(completion.choices[0].message.content)
