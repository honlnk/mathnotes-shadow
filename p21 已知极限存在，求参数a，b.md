### 题目回顾

我们有一个分段函数：

$$ f(x) = \begin{cases} 
a x^{2} + b, & x \geq 1 \\
x \cos \frac{\pi}{2} x, & x < 1 
\end{cases} $$

要求在 $\displaystyle x = 1$ 处函数 $\displaystyle f(x)$ 可导，求 $\displaystyle a$ 和 $\displaystyle b$ 的值。

### 理解题意

首先，我需要理解什么是函数在某一点可导。函数在某点可导意味着在该点的左导数和右导数存在且相等。对于分段函数，我们需要确保在分段点 $\displaystyle x = 1$ 处，函数值和导数值都连续。

### 步骤一：确保函数在 $\displaystyle x = 1$ 处连续

函数在 $\displaystyle x = 1$ 处连续，意味着：

$$ \lim_{x \to 1^-} f(x) = \lim_{x \to 1^+} f(x) = f(1) $$

计算左右极限：

1. 当 $\displaystyle x \to 1^-$ 时，$\displaystyle x < 1$，使用 $\displaystyle f(x) = x \cos \frac{\pi}{2} x$：

$$ \lim_{x \to 1^-} f(x) = 1 \cdot \cos \frac{\pi}{2} \cdot 1 = 1 \cdot \cos \frac{\pi}{2} = 1 \cdot 0 = 0 $$

2. 当 $\displaystyle x \to 1^+$ 时，$\displaystyle x \geq 1$，使用 $\displaystyle f(x) = a x^2 + b$：

$$ \lim_{x \to 1^+} f(x) = a \cdot 1^2 + b = a + b $$

3. 函数在 $\displaystyle x = 1$ 处的值：

$$ f(1) = a \cdot 1^2 + b = a + b $$

为了函数在 $\displaystyle x = 1$ 处连续，必须有：

$$ \lim_{x \to 1^-} f(x) = \lim_{x \to 1^+} f(x) = f(1) $$

即：

$$ 0 = a + b $$

所以，我们得到第一个方程：

$$ a + b = 0 \quad (1) $$

### 步骤二：确保函数在 $\displaystyle x = 1$ 处可导

函数在 $\displaystyle x = 1$ 处可导，意味着左导数和右导数存在且相等。

1. 计算左导数 $\displaystyle f'_{-}(1)$：

当 $\displaystyle x < 1$，$\displaystyle f(x) = x \cos \frac{\pi}{2} x$，求导：

$$ f'(x) = \cos \frac{\pi}{2} x + x \cdot \left( -\frac{\pi}{2} \sin \frac{\pi}{2} x \right) = \cos \frac{\pi}{2} x - \frac{\pi}{2} x \sin \frac{\pi}{2} x $$

在 $\displaystyle x = 1^-$ 处：

$$ f'_{-}(1) = \cos \frac{\pi}{2} \cdot 1 - \frac{\pi}{2} \cdot 1 \cdot \sin \frac{\pi}{2} \cdot 1 = \cos \frac{\pi}{2} - \frac{\pi}{2} \sin \frac{\pi}{2} = 0 - \frac{\pi}{2} \cdot 1 = -\frac{\pi}{2} $$

2. 计算右导数 $\displaystyle f'_{+}(1)$：

当 $\displaystyle x \geq 1$，$\displaystyle f(x) = a x^2 + b$，求导：

$$ f'(x) = 2a x $$

在 $\displaystyle x = 1^+$ 处：

$$ f'_{+}(1) = 2a \cdot 1 = 2a $$

为了函数在 $\displaystyle x = 1$ 处可导，必须有：

$$ f'_{-}(1) = f'_{+}(1) $$

即：

$$ -\frac{\pi}{2} = 2a $$

解这个方程，得到：

$$ a = -\frac{\pi}{4} $$

### 步骤三：求解 $\displaystyle b$

根据方程 (1)：

$$ a + b = 0 $$

已知 $\displaystyle a = -\frac{\pi}{4}$，代入得：

$$ -\frac{\pi}{4} + b = 0 $$

解得：

$$ b = \frac{\pi}{4} $$

### 最终答案

经过以上步骤，我们得到：

$$ a = -\frac{\pi}{4} $$
$$ b = \frac{\pi}{4} $$

所以，答案是：

$$ a = \boxed{-\dfrac{\pi}{4}} $$
$$ b = \boxed{\dfrac{\pi}{4}} $$