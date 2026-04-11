---
concept: Sum of Ideals
slug: sum-of-ideals
category: ring-theory
subcategory: ideals
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 247
section: "7.3 Ring Homomorphisms and Quotient Rings"
extraction_confidence: high
aliases: []
prerequisites:
  - ideal
extends: []
related:
  - product-of-ideals
  - comaximal-ideals
contrasts_with: []
answers_questions:
  - "What is the sum of two ideals?"
---

# Quick Definition
The sum $I + J$ of ideals I and J is $\{a + b \mid a \in I, b \in J\}$, the smallest ideal containing both I and J.

# Core Definition
The *sum* of ideals I and J is $I + J = \{a + b \mid a \in I, b \in J\}$. This is the smallest ideal of R containing both I and J (Dummit & Foote, p. 248).

# Prerequisites
- **Ideal** — Sum is defined for ideals

# Key Properties
1. $I + J$ is an ideal (p. 248)
2. $I + J$ is the smallest ideal containing both I and J
3. In $\mathbb{Z}$: $m\mathbb{Z} + n\mathbb{Z} = d\mathbb{Z}$ where $d = \gcd(m, n)$ (p. 248)
4. I and J are comaximal iff $I + J = R$

# Construction / Recognition
## To Construct:
1. Take all sums $a + b$ with $a \in I$ and $b \in J$

# Context & Application
The sum of ideals is the ideal-theoretic analogue of the least common supergroup.

# Examples
**Example 1** (p. 248): $6\mathbb{Z} + 10\mathbb{Z} = 2\mathbb{Z}$ since $\gcd(6, 10) = 2$.

# Relationships

## Related
- **product-of-ideals** — $IJ \subseteq I \cap J \subseteq I + J$ in general
- **comaximal-ideals** — $I + J = R$ means I and J are comaximal

# Common Errors
- **Error**: Confusing $I + J$ with $I \cup J$
  **Correction**: $I \cup J$ is generally not an ideal; $I + J$ takes all sums

# Common Confusions
- **Confusion**: Thinking $I + J$ adds the generating sets
  **Clarification**: $I + J$ consists of all sums $a + b$, not just generators

# Source Reference
Chapter 7, Section 7.3, Definition (1), page 248.

# Verification Notes
- Definition: Direct from p. 248
- Confidence: HIGH — explicit definition
