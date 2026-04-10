---
# === CORE IDENTIFICATION ===
concept: Strongly Regular Graph
slug: strongly-regular-graph

# === CLASSIFICATION ===
category: spectral-graph-theory
subcategory: highly-symmetric-graphs
tier: advanced

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 277
section: "VIII.3 Strongly Regular Graphs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - srg

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eigenvalue-of-graph
  - adjacency-matrix
extends:
  - highly-regular-graph
related:
  - rationality-condition
  - hoffman-singleton-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a strongly regular graph?"
---

# Quick Definition

A strongly regular graph with parameters $(k, a, b)$ is a $k$-regular incomplete graph where any two adjacent vertices have exactly $a$ common neighbors and any two non-adjacent vertices have exactly $b \ge 1$ common neighbors.

# Core Definition

A graph $G$ is strongly regular with parameters $(k, a, b)$ if it is a $k$-regular incomplete graph such that any two adjacent vertices have exactly $a \ge 0$ common neighbors and any two non-adjacent vertices have exactly $b \ge 1$ common neighbors (Bollobas, p. 277). Equivalently: $A^2 = kI + aA + b(J - I - A)$ where $A, I, J$ are $n \times n$ matrices. **Theorem 17**: A connected incomplete regular graph is strongly regular iff it has precisely three distinct eigenvalues.

# Prerequisites

- **Eigenvalue of a graph** -- Characterized by having 3 distinct eigenvalues
- **Adjacency matrix** -- The algebraic framework

# Key Properties

1. Parameters: order $n$, degree $k$, $a$ common neighbors for adjacent pairs, $b$ for non-adjacent
2. Has exactly 3 distinct eigenvalues: $k$, $\mu_1$, $\mu_2$
3. $\mu_{1,2} = \frac{1}{2}\{a-b \pm \sqrt{(a-b)^2 + 4(k-b)}\}$ (from the collapsed adjacency matrix)
4. The multiplicities $m_1, m_2$ must be natural numbers (rationality condition)
5. Collapsed adjacency matrix is $3 \times 3$

# Construction / Recognition

## To Verify Strong Regularity
1. Check $G$ is $k$-regular and incomplete
2. For every edge $uv$: count $|\Gamma(u) \cap \Gamma(v)| = a$
3. For every non-edge $uv$: count $|\Gamma(u) \cap \Gamma(v)| = b$
4. Verify $b \ge 1$

# Context & Application

Strongly regular graphs arise in combinatorial design theory, coding theory, and the classification of finite simple groups. They include Petersen graph (parameters 3, 0, 1), Paley graphs, and graphs associated with sporadic simple groups.

# Examples

**Example 1** (p. 278, Fig. VIII.11): The pentagon (5, 2, 0, 1), the cube (8, 3, 0, 1), and the Petersen graph (10, 3, 0, 1).

**Example 2** (p. 283): A strongly regular graph with parameters (162, 105, 81) related to the McLaughlin group.

# Relationships

## Builds Upon
- **Eigenvalue of a graph** -- Spectral characterization
- **Adjacency matrix** -- Algebraic framework
- **Highly regular graph** -- Generalization

## Enables
- **Rationality condition** -- Multiplicity constraint
- **Hoffman-Singleton theorem** -- Classifies Moore graphs

## Related
- **Rationality condition** -- Necessary condition for existence
- **Hoffman-Singleton theorem** -- Classification of certain srg's

## Contrasts With
- None

# Common Errors

- **Error**: Forgetting the condition $b \ge 1$
  **Correction**: $b \ge 1$ is required; complete multipartite graphs have $b = 0$ but are not considered strongly regular

# Common Confusions

- **Confusion**: Thinking strongly regular means vertex-transitive
  **Clarification**: Strong regularity is a purely combinatorial condition on neighbor counts; it does not require transitivity

# Source Reference

Chapter VIII, Section VIII.3, pages 277--283. Theorems 17, 18, 19.

# Verification Notes

- Definition source: Direct from p. 277
- Confidence rationale: Explicit definition with characterization theorem
- Uncertainties: None
- Cross-reference status: Verified
