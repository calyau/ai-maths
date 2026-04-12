---
# === CORE IDENTIFICATION ===
concept: Counting Theorem
slug: counting-theorem

# === CLASSIFICATION ===
category: group-actions
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Counting Orbits"
chapter_number: 18
pdf_page: 105
section: "Theorem 18.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Burnside's lemma"
  - "Cauchy-Frobenius lemma"
  - "Burnside counting theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
  - orbit-stabilizer-theorem
  - fixed-point-set
extends: []
related:
  - conjugate-fixed-point-sets
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I count orbits using the Counting Theorem (Burnside's lemma)?"
  - "What is the average number of fixed points?"
---

# Quick Definition

The number of distinct orbits of a finite group $G$ acting on a set $X$ equals the average number of points left fixed by an element of $G$: $\frac{1}{|G|} \sum_{g \in G} |X^g|$.

# Core Definition

**(18.1) The Counting Theorem.** The number of distinct orbits is

$$\frac{1}{|G|} \sum_{g \in G} |X^g|$$

in other words, the average number of points left fixed by an element of $G$ (Armstrong, p. 105).

Armstrong calls this result the "Counting Theorem" rather than "Burnside's lemma."

# Prerequisites

- **Group action** -- the theorem applies to an action of a finite group on a set
- **Orbit-Stabilizer theorem** -- used in the proof to relate $|G_x|$ to orbit sizes
- **Fixed-point set** -- $X^g$ appears in the formula

# Key Properties

1. The sum $\sum_{g \in G} |X^g|$ equals $\sum_{x \in X} |G_x|$ (double counting)
2. Each orbit contributes exactly $|G|$ to $\sum_{x \in X_i} |G_x|$ (by Orbit-Stabilizer)
3. If there are $k$ orbits, then $\sum_{x \in X} |G_x| = k|G|$
4. Conjugate elements contribute equally to the sum (Theorem 18.2)

# Construction / Recognition

## Proof Sketch (p. 106):
1. Count pairs $(g, x) \in G \times X$ with $g(x) = x$ in two ways
2. Grouping by $g$: the count is $\sum_{g \in G} |X^g|$
3. Grouping by $x$: the count is $\sum_{x \in X} |G_x|$
4. Partition $X$ into orbits $X_1, \ldots, X_k$ and rewrite: $\sum_{i=1}^{k} \sum_{x \in X_i} |G_x|$
5. Within orbit $X_i$, all stabilizers have the same order, so $\sum_{x \in X_i} |G_x| = |X_i| \cdot |G_{\bar{x}}| = |G|$
6. Therefore $\sum |X^g| = k|G|$, giving $k = \frac{1}{|G|} \sum |X^g|$

## To Apply the Counting Theorem:
1. Identify the group $G$ and the set $X$ being acted upon
2. List the conjugacy classes of $G$ with their sizes
3. For a representative $g$ of each conjugacy class, compute $|X^g|$
4. Sum: $\text{(class size)} \times |X^g|$ over all classes
5. Divide by $|G|$

# Context & Application

The Counting Theorem is the principal tool for solving combinatorial problems involving symmetry, such as counting distinct colourings of geometric objects. Armstrong motivates it with Emily's and Jerome's cube-colouring problems.

# Examples

**Emily's Problem** (p. 106): Painting each face of a cube either red or green, the number of genuinely different coloured cubes is:
$$\frac{1}{24}\{(6 \times 2^3) + (3 \times 2^4) + (8 \times 2^2) + (6 \times 2^3) + 2^6\} = 10$$

**Jerome's Problem** (p. 107): Painting stripes on cube faces (symmetry group $A_4$, not $S_4$):
$$\frac{1}{12}\{(3 \times 2^4) + (4 \times 2^2) + (4 \times 2^2) + 2^6\} = 12$$

**Mobius Band** (p. 107): Painting 10 squares of a Mobius band with 3 colours (symmetry group $D_{10}$):
$$\frac{1}{20}\{3^{10} + 2 \cdot 3 + 2 \cdot 3^2 + 2 \cdot 3 + 2 \cdot 3^2 + 3^5 + 5 \cdot 3^6 + 5 \cdot 3^5\} = 3210$$

# Relationships

## Builds Upon
- **Orbit-Stabilizer theorem** -- key step in the proof
- **Fixed-point set** -- $|X^g|$ appears directly in the formula
- **Group action** -- the setting for the theorem

## Enables
- **Colouring problems** -- counting distinct colourings up to symmetry
- **Classification of finite rotation groups** -- used in the proof of Theorem 19.2

## Related
- **Conjugate fixed-point sets** -- Theorem 18.2 allows computation by conjugacy classes

# Common Errors

- **Error**: Forgetting to weight each $|X^g|$ by the size of its conjugacy class.
  **Correction**: The sum is over all $g \in G$, which means each conjugacy class representative's $|X^g|$ is multiplied by the class size.

- **Error**: Using the wrong symmetry group (e.g., full symmetry group instead of the relevant subgroup).
  **Correction**: As Jerome's problem shows, the relevant group depends on which symmetries preserve the structure being decorated.

# Common Confusions

- **Confusion**: The name "Burnside's lemma" -- Burnside himself attributed the result to Cauchy and Frobenius.
  **Clarification**: Armstrong calls it the "Counting Theorem" (18.1), avoiding the attribution issue.

# Source Reference

Chapter 18: Counting Orbits, Theorem 18.1, pages 105--108. Proof on pp. 105--106. Emily's problem pp. 106--107, Jerome's problem p. 107, Mobius band pp. 107--108.

# Verification Notes

- Theorem and proof: Direct from pp. 105--106
- All three worked examples: Direct from source
- Confidence: HIGH -- central theorem with full proof and multiple applications
