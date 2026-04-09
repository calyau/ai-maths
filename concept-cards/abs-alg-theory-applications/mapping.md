---
# === CORE IDENTIFICATION ===
concept: Mapping
slug: mapping

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
  - function
  - map

# === TYPED RELATIONSHIPS ===
prerequisites:
  - relation
  - cartesian-product
extends:
  - relation
related:
  - well-defined-function
  - injective-function
  - surjective-function
contrasts_with:
  - relation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

A mapping (or function) $f: A \to B$ is a special type of relation where each element $a \in A$ has a unique element $b \in B$ such that $f(a) = b$.

# Core Definition

"We will define a mapping or function $f \subset A \times B$ from a set $A$ to a set $B$ to be the special type of relation where each element $a \in A$ has a unique element $b \in B$ such that $(a, b) \in f$" (Judson, p. 19). The set $A$ is called the **domain** of $f$ and $f(A) = \{f(a) : a \in A\} \subset B$ is called the **range** or **image** of $f$.

# Prerequisites

- **Relation** — A mapping is a special type of relation
- **Cartesian product** — A mapping is a subset of $A \times B$

# Key Properties

1. Each element of the domain maps to exactly one element of the codomain
2. Every element of the domain must be assigned a value
3. The image $f(A)$ may be a proper subset of $B$
4. We write $f: A \to B$ or $f(a) = b$ or $f: a \mapsto b$

# Construction / Recognition

## To Verify a Relation is a Mapping:
1. Check that every element of $A$ is assigned a value
2. Check that each element of $A$ is assigned to exactly one element of $B$
3. If either condition fails, the relation is not a mapping

# Context & Application

Mappings are the foundation for defining group homomorphisms, isomorphisms, and binary operations. A binary operation on a group $G$ is a mapping from $G \times G$ to $G$.

# Examples

**Example 1** (p. 20): Given $A = \{1, 2, 3\}$ and $B = \{a, b, c\}$, a relation $f$ with $f(1) = a$, $f(2) = b$, $f(3) = c$ is a mapping. But a relation $g$ with $g(1) = a$ and $g(1) = b$ is not, since 1 is assigned to two elements.

**Example 2** (p. 20): $f: \mathbb{R} \to \mathbb{R}$ defined by $f(x) = x^3$ is a mapping.

# Relationships

## Builds Upon
- **relation** — A mapping is a special case of a relation

## Enables
- **injective-function** — A mapping with the one-to-one property
- **surjective-function** — A mapping with the onto property
- **function-composition** — Composing mappings
- **binary-operation** — A map $G \times G \to G$

## Contrasts With
- **relation** — A relation need not assign unique values

# Common Errors

- **Error**: Defining a function that assigns different outputs to equivalent inputs
  **Correction**: The function must be well-defined: if $a_1 = a_2$, then $f(a_1) = f(a_2)$

# Common Confusions

- **Confusion**: Confusing the range (image) with the codomain
  **Clarification**: The range $f(A) \subset B$ may be a proper subset of the codomain $B$

# Source Reference

Chapter 1: Preliminaries, Section 1.2, pages 19-20.

# Verification Notes

- Definition source: Direct quote from p. 19
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
