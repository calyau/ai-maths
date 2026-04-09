---
# === CORE IDENTIFICATION ===
concept: Cartesian Product
slug: cartesian-product

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
pdf_page: 19
section: "Cartesian Products and Mappings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - direct product of sets

# === TYPED RELATIONSHIPS ===
prerequisites:
  - set
extends: []
related:
  - relation
  - mapping
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

The Cartesian product of sets $A$ and $B$, denoted $A \times B$, is the set of all ordered pairs $(a, b)$ where $a \in A$ and $b \in B$.

# Core Definition

"Given sets $A$ and $B$, we can define a new set $A \times B$, called the Cartesian product of $A$ and $B$, as a set of ordered pairs. That is, $A \times B = \{(a, b) : a \in A \text{ and } b \in B\}$" (Judson, p. 19). More generally, the Cartesian product of $n$ sets is $A_1 \times \cdots \times A_n = \{(a_1, \ldots, a_n) : a_i \in A_i\}$.

# Prerequisites

- **Set** — Cartesian product is constructed from sets

# Key Properties

1. $A \times \emptyset = \emptyset$ for any set $A$
2. In general, $A \times B \neq B \times A$ (ordered pairs are ordered)
3. If $A$ has $m$ elements and $B$ has $n$ elements, then $A \times B$ has $mn$ elements
4. $A^n$ denotes $A \times \cdots \times A$ ($n$ times)

# Construction / Recognition

## To Construct $A \times B$:
1. For each element $a \in A$ and each element $b \in B$, form the ordered pair $(a, b)$
2. Collect all such pairs

# Context & Application

Cartesian products are essential for defining relations and functions. A binary operation on a group $G$ is formally a function $G \times G \to G$. The set $\mathbb{R}^2 = \mathbb{R} \times \mathbb{R}$ represents the Euclidean plane.

# Examples

**Example 1** (p. 19): If $A = \{x, y\}$ and $B = \{1, 2, 3\}$, then $A \times B = \{(x,1), (x,2), (x,3), (y,1), (y,2), (y,3)\}$.

**Example 2** (p. 19): $\mathbb{R}^3$ consists of all 3-tuples of real numbers.

# Relationships

## Builds Upon
- **set** — Constructed from sets

## Enables
- **relation** — Relations are subsets of $A \times B$
- **mapping** — Functions are special relations on $A \times B$
- **binary-operation** — A binary operation is a map $G \times G \to G$

# Common Errors

- **Error**: Forgetting that order matters in $(a, b)$
  **Correction**: $(a, b) \neq (b, a)$ in general, so $A \times B \neq B \times A$

# Common Confusions

- **Confusion**: Confusing Cartesian product with union
  **Clarification**: $A \times B$ produces ordered pairs; $A \cup B$ collects individual elements

# Source Reference

Chapter 1: Preliminaries, Section 1.2, page 19.

# Verification Notes

- Definition source: Direct quote from p. 19
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
