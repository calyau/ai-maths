---
# === CORE IDENTIFICATION ===
concept: Similar Matrices
slug: similar-matrices

# === CLASSIFICATION ===
category: foundations
subcategory: set-theory
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Preliminaries"
chapter_number: 1
pdf_page: 25
section: "Equivalence Relations and Partitions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - matrix similarity

# === TYPED RELATIONSHIPS ===
prerequisites:
  - equivalence-relation
  - general-linear-group
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

Two matrices $A$ and $B$ are similar if there exists an invertible matrix $P$ such that $PAP^{-1} = B$. Similarity is an equivalence relation on matrices.

# Core Definition

"We can define an equivalence relation on the set of $2 \times 2$ matrices, by saying $A \sim B$ if there exists an invertible matrix $P$ such that $PAP^{-1} = B$... Two matrices that are equivalent in this manner are said to be similar" (Judson, p. 25).

# Prerequisites

- **Equivalence relation** — Similarity is an equivalence relation
- **General linear group** — $P$ must be invertible ($P \in GL_2(\mathbb{R})$)

# Key Properties

1. Reflexive: $IAI^{-1} = A$
2. Symmetric: If $PAP^{-1} = B$, then $A = P^{-1}B(P^{-1})^{-1}$
3. Transitive: If $PAP^{-1} = B$ and $QBQ^{-1} = C$, then $(QP)A(QP)^{-1} = C$

# Examples

**Example 1** (p. 25): $A = \begin{pmatrix} 1 & 2 \\ -1 & 1 \end{pmatrix} \sim B = \begin{pmatrix} -18 & 33 \\ -11 & 20 \end{pmatrix}$ with $P = \begin{pmatrix} 2 & 5 \\ 1 & 3 \end{pmatrix}$.

# Relationships

## Builds Upon
- **equivalence-relation** — Similarity is an equivalence relation

# Context & Application

Matrix similarity preserves eigenvalues and other invariants. Similar matrices represent the same linear transformation in different bases. This equivalence relation partitions matrices into similarity classes.

# Source Reference

Chapter 1: Preliminaries, Section 1.2, Example 1.24, page 25.

# Verification Notes

- Definition source: Direct from p. 25
- Confidence: HIGH — explicit definition and verification
- Cross-reference status: Verified
- Uncertainties: None
