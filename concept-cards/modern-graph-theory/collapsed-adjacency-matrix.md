---
# === CORE IDENTIFICATION ===
concept: Collapsed Adjacency Matrix
slug: collapsed-adjacency-matrix

# === CLASSIFICATION ===
category: spectral-graph-theory
subcategory: matrix-representations
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 278
section: "VIII.3 Strongly Regular Graphs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - highly-regular-graph
  - adjacency-matrix
extends: []
related:
  - strongly-regular-graph
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I compute eigenvalues of a highly regular graph efficiently?"
---

# Quick Definition

The collapsed adjacency matrix $C$ of a highly regular graph is a small $p \times p$ matrix that shares the same minimal polynomial (and thus eigenvalues) as the full $n \times n$ adjacency matrix $A$.

# Core Definition

For a highly regular graph with partition $V_1 = \{x\}, V_2, \ldots, V_p$ at each vertex, $c_{ij} = \sum_{v_t \in V_i} a_{st}$ for $v_s \in V_j$ (independent of the choice of representative $v_s$). **Theorem 15** (Bollobas, p. 279): $\pi_r A = C\pi_r$, and $A$ and $C$ have the same minimal polynomial. In particular, $\mu$ is an eigenvalue of $A$ iff it is a root of $\det(C - \mu I) = 0$.

# Prerequisites

- **Highly regular graph** -- Defines the collapsed matrix
- **Adjacency matrix** -- The full matrix being collapsed

# Key Properties

1. $C$ is $p \times p$ while $A$ is $n \times n$ (typically $p \ll n$)
2. $A$ and $C$ have the same minimal polynomial
3. For strongly regular graphs: $C$ is $3 \times 3$
4. Column sums of $C$ equal $k$ (the degree)

# Construction / Recognition

## To Form the Collapsed Matrix
1. Fix a vertex $x$ and the partition $V_1 = \{x\}, V_2, \ldots, V_p$
2. For each $i, j$: $c_{ij} = $ number of neighbors in $V_i$ of any vertex in $V_j$
3. Verify this is independent of the choice of vertex in $V_j$

# Context & Application

The collapsed adjacency matrix reduces the eigenvalue computation for highly regular graphs from an $n \times n$ problem to a $p \times p$ problem. For strongly regular graphs ($p = 3$), the eigenvalues can be found by solving a quadratic.

# Examples

**Example** (p. 278, Fig. VIII.11): The Petersen graph has collapsed adjacency matrix $\begin{pmatrix} 0 & 1 & 0 \\ 3 & 0 & 1 \\ 0 & 2 & 2 \end{pmatrix}$.

# Relationships

## Builds Upon
- **Highly regular graph** -- Defines the partition
- **Adjacency matrix** -- Being collapsed

## Enables
- **Strongly regular graph** -- The $3 \times 3$ case
- **Rationality condition** -- Eigenvalues from $C$

## Related
- **Strongly regular graph** -- $C$ is $3 \times 3$

## Contrasts With
- None

# Common Errors

- **Error**: Expecting $C$ to determine the graph uniquely
  **Correction**: Many non-isomorphic graphs can have the same collapsed adjacency matrix

# Common Confusions

- **Confusion**: Thinking $C$ has the same eigenvalues with the same multiplicities as $A$
  **Clarification**: $C$ and $A$ share the same minimal polynomial; eigenvalues are the same but multiplicities differ

# Source Reference

Chapter VIII, Section VIII.3, Theorem 15, pages 278--280.

# Verification Notes

- Definition source: Direct from pp. 278--279
- Confidence rationale: Explicit definition with theorem
- Uncertainties: None
- Cross-reference status: Verified
