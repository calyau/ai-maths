---
concept: Solvable Group
slug: solvable-group
category: group-structure
subcategory: group-classification
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Structure of Groups"
chapter_number: 13
pdf_page: 178
section: "Solvable Groups"
extraction_confidence: high
aliases:
  - "soluble group"
prerequisites:
  - subnormal-series
  - factor-group
  - normal-subgroup
extends: []
related:
  - simple-group
  - commutator-subgroup
  - derived-series
  - composition-series
contrasts_with:
  - simple-group
answers_questions:
  - "What is a solvable group?"
  - "What distinguishes a simple group from a solvable group?"
  - "Why are solvable groups important for polynomial equations?"
---

# Quick Definition

A group $G$ is solvable if it has a subnormal series $G = H_n \supset \cdots \supset H_0 = \{e\}$ such that all factor groups $H_{i+1}/H_i$ are abelian. Solvable groups are central to the study of polynomial equations.

# Core Definition

"A group $G$ is **solvable** if it has a subnormal series $\{H_i\}$ such that all of the factor groups $H_{i+1}/H_i$ are abelian" (Judson, p. 178).

# Prerequisites

- **Subnormal series** — Solvability is defined via subnormal series
- **Factor group** — The factor groups must be abelian
- **Normal subgroup** — Required for factor groups to exist

# Key Properties

1. Every abelian group is solvable (use the trivial series)
2. $S_4$ is solvable: $S_4 \supset A_4 \supset V_4 \supset \{(1)\}$ with abelian factors
3. $S_n$ is NOT solvable for $n \geq 5$ (since $A_n$ is simple and nonabelian)
4. $G$ is solvable iff $G^{(n)} = \{e\}$ for some $n$ (derived series)
5. Subgroups and quotients of solvable groups are solvable

# Construction / Recognition

## To Determine if $G$ is Solvable:
1. Try to find a subnormal series with abelian factors
2. Alternatively, compute the derived series $G \supset G' \supset G'' \supset \cdots$
3. $G$ is solvable iff the derived series reaches $\{e\}$
4. For $S_n$: solvable iff $n \leq 4$

# Context & Application

"Solvable groups will play a fundamental role when we study Galois theory and the solution of polynomial equations" (p. 175). A polynomial equation is solvable by radicals if and only if its Galois group is solvable. Since $S_5$ is not solvable, the general quintic cannot be solved by radicals.

# Examples

**Example 1** (p. 178): $S_4$ is solvable: $S_4 \supset A_4 \supset \{(1),(12)(34),(13)(24),(14)(23)\} \supset \{(1)\}$ has abelian factor groups.

**Example 2** (p. 178): For $n \geq 5$, $S_n$ is not solvable since $S_n \supset A_n \supset \{(1)\}$ is a composition series with $A_n$ nonabelian.

# Relationships

## Builds Upon
- **Subnormal series** — Solvability is defined via such series
- **Factor group** — Factors must be abelian

## Enables
- **Galois theory** — Solvability by radicals requires solvable Galois group

## Related
- **Commutator subgroup** — $G$ is solvable iff the derived series terminates
- **Composition series** — If all composition factors are cyclic of prime order, the group is solvable

## Contrasts With
- **Simple group** — Simple nonabelian groups are not solvable

# Common Confusions

- **Confusion**: Thinking "solvable" relates to solving a mathematical problem in general
  **Clarification**: "Solvable" specifically relates to whether a polynomial equation can be solved by radicals, through Galois theory

# Source Reference

Chapter 13: The Structure of Groups, Section 13.2, p. 178. Examples 13.19.

# Verification Notes

- Definition source: Direct quote from p. 178
- Confidence: HIGH — explicit definition
