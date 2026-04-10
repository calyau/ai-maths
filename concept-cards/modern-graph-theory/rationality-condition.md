---
# === CORE IDENTIFICATION ===
concept: Rationality Condition
slug: rationality-condition

# === CLASSIFICATION ===
category: spectral-graph-theory
subcategory: strongly-regular-constraints
tier: advanced

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 281
section: "VIII.3 Strongly Regular Graphs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - multiplicity condition for strongly regular graphs

# === TYPED RELATIONSHIPS ===
prerequisites:
  - strongly-regular-graph
extends: []
related:
  - hoffman-singleton-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What algebraic conditions must the parameters of a strongly regular graph satisfy?"
---

# Quick Definition

For a strongly regular graph with parameters $(n, k, a, b)$, the multiplicities $m_{1,2} = \frac{1}{2}\{n-1 \pm \frac{(n-1)(b-a)-2k}{\sqrt{(a-b)^2+4(k-b)}}\}$ must be natural numbers.

# Core Definition

**Theorem 18** (Bollobas, p. 281): If there is a strongly regular graph of order $n$ with parameters $(k, a, b)$, then $m_1, m_2 = \frac{1}{2}\{n-1 \pm \frac{(n-1)(b-a)-2k}{\sqrt{(a-b)^2+4(k-b)}}\}$ are natural numbers. These are the multiplicities of the non-principal eigenvalues $\mu_{1,2} = \frac{1}{2}\{a-b \pm \sqrt{(a-b)^2+4(k-b)}\}$.

# Prerequisites

- **Strongly regular graph** -- The object constrained

# Key Properties

1. Severely restricts which parameter tuples $(n, k, a, b)$ can be realized
2. Either $(a-b)^2 + 4(k-b)$ is a perfect square, or $m_1 = m_2 = (n-1)/2$ (conference graphs)
3. Combined with $m_1 + m_2 = n - 1$ and $m_1\mu_1 + m_2\mu_2 = -k$
4. The key tool for the Hoffman-Singleton theorem

# Construction / Recognition

## To Check the Rationality Condition
1. Compute $\mu_{1,2}$ from the collapsed adjacency matrix
2. Compute $m_1, m_2$ from the formula
3. Verify both are positive integers

# Context & Application

The rationality condition is the primary algebraic obstruction to the existence of strongly regular graphs. It rules out most parameter tuples and is the basis of the Hoffman-Singleton classification of Moore graphs of diameter 2.

# Examples

**Example** (p. 282): For Moore graphs with $(k, 0, 1)$: $4k - 3$ must be a perfect square $s^2$, and $s | 15$, giving $k \in \{2, 3, 7, 57\}$.

# Relationships

## Builds Upon
- **Strongly regular graph** -- The context

## Enables
- **Hoffman-Singleton theorem** -- Direct application

## Related
- **Hoffman-Singleton theorem** -- Classification result

## Contrasts With
- None

# Common Errors

- **Error**: Assuming the rationality condition is sufficient for existence
  **Correction**: It is necessary but not sufficient; additional conditions may be needed (e.g., $k = 57$ passes rationality but existence is unknown)

# Common Confusions

- **Confusion**: Thinking the condition only involves rationality of eigenvalues
  **Clarification**: The eigenvalues can be irrational; the condition is that their multiplicities must be natural numbers

# Source Reference

Chapter VIII, Section VIII.3, Theorem 18, pages 281--282.

# Verification Notes

- Definition source: Direct from Theorem 18
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
