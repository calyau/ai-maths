---
# === CORE IDENTIFICATION ===
concept: Binary Operation
slug: binary-operation

# === CLASSIFICATION ===
category: group-theory
subcategory: group-definitions
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Groups"
chapter_number: 3
pdf_page: 46
section: "Definitions and Examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - law of composition

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mapping
  - cartesian-product
extends: []
related:
  - group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
  - "How do I determine if a set with an operation forms a group?"
---

# Quick Definition

A binary operation (or law of composition) on a set $G$ is a function $G \times G \to G$ that assigns to each pair $(a, b)$ a unique element $a \circ b$ in $G$.

# Core Definition

"A binary operation or law of composition on a set $G$ is a function $G \times G \to G$ that assigns to each pair $(a, b) \in G \times G$ a unique element $a \circ b$, or $ab$ in $G$, called the composition of $a$ and $b$" (Judson, p. 46).

# Prerequisites

- **Mapping** — A binary operation is a function
- **Cartesian product** — The domain is $G \times G$

# Key Properties

1. Takes two inputs from $G$ and produces one output in $G$
2. The output must be in $G$ (closure)
3. Each pair maps to exactly one element (well-defined)
4. May or may not be commutative
5. May or may not be associative

# Construction / Recognition

## To Verify a Binary Operation on $G$:
1. Check that for every pair $(a, b) \in G \times G$, the result $a \circ b$ is defined
2. Check that $a \circ b \in G$ for all $a, b \in G$ (closure)
3. Check that the result is unique (well-defined)

# Context & Application

A binary operation is the essential ingredient for defining a group. The group axioms (associativity, identity, inverses) are conditions on the binary operation. Common binary operations include addition, multiplication, function composition, and matrix multiplication.

# Examples

**Example 1** (p. 47): Addition modulo $n$ on $\mathbb{Z}_n$ is a binary operation.

**Example 2** (p. 48): Matrix multiplication on $GL_2(\mathbb{R})$ is a binary operation.

**Example 3** (p. 46): Composition of symmetries is a binary operation on the set of symmetries of a triangle.

# Relationships

## Builds Upon
- **mapping** — A binary operation is a function $G \times G \to G$

## Enables
- **group** — A group is a set with a binary operation satisfying the group axioms

# Common Errors

- **Error**: Forgetting to verify closure (that the result stays in $G$)
  **Correction**: Always check $a \circ b \in G$ for all $a, b \in G$

# Common Confusions

- **Confusion**: Assuming a binary operation must be commutative
  **Clarification**: Commutativity is not required; matrix multiplication and function composition are non-commutative binary operations

# Source Reference

Chapter 3: Groups, Section 3.2, page 46.

# Verification Notes

- Definition source: Direct quote from p. 46
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
