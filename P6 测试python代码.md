根据**拉格朗日中值定理**，如果函数 $\displaystyle f(x)$ 满足以下条件：
1. 在闭区间 $\displaystyle [a, b]$ 上连续；
2. 在开区间 $\displaystyle (a, b)$ 内可导，

那么存在一个点 $\displaystyle c \in (a, b)$，使得
$$
f(b) - f(a) = f'(c)(b - a).
$$

在本题中，我们定义函数 $\displaystyle f(x) = \arctan x$。接下来，我们验证 $\displaystyle f(x)$ 是否满足拉格朗日中值定理的条件：

---

### 1. **连续性**：
函数 $\displaystyle f(x) = \arctan x$ 在其定义域 $\displaystyle (-\infty, +\infty)$ 上是连续的。因此，$\displaystyle f(x)$ 在闭区间 $\displaystyle [a, b]$ 上连续。

---

### 2. **可导性**：
函数 $\displaystyle f(x) = \arctan x$ 的导数为
$$
f'(x) = \frac{1}{1 + x^{2}}.
$$
这个导数在 $\displaystyle (-\infty, +\infty)$ 上处处存在且连续。因此，$\displaystyle f(x)$ 在开区间 $\displaystyle (a, b)$ 内可导。

---

### 3. **应用中值定理**：
既然 $\displaystyle f(x) = \arctan x$ 满足拉格朗日中值定理的条件，那么根据定理，存在一个点 $\displaystyle c \in (a, b)$，使得
$$
f(b) - f(a) = f'(c)(b - a).
$$

将 $\displaystyle f(x) = \arctan x$ 和 $\displaystyle f'(x) = \frac{1}{1 + x^{2}}$ 代入，得到
$$
\arctan b - \arctan a = \frac{1}{1 + c^{2}} \cdot (b - a).
$$

整理后，即为
$$
\arctan b - \arctan a = \frac{b - a}{1 + c^{2}}.
$$

---

### 4. **为什么 $\displaystyle c \in (a, b)$**：
拉格朗日中值定理明确指出，点 $\displaystyle c$ 位于开区间 $\displaystyle (a, b)$ 内，即 $\displaystyle c \in (a, b)$。这是因为定理的条件要求 $\displaystyle f(x)$ 在 $\displaystyle (a, b)$ 内可导，而 $\displaystyle c$ 是导数值 $\displaystyle f'(c)$ 与平均变化率 $\displaystyle \frac{f(b) - f(a)}{b - a}$ 相等的点。

---

### 总结：
根据拉格朗日中值定理，存在一个 $\displaystyle c \in (a, b)$，使得
$$
\arctan b - \arctan a = \frac{b - a}{1 + c^{2}}.
$$
这是因为 $\displaystyle f(x) = \arctan x$ 满足定理的条件，且 $\displaystyle f'(x) = \frac{1}{1 + x^{2}}$。