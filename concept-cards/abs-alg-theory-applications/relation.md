---
# === CORE IDENTIFICATION ===
concept: Relation
slug: relation

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cartesian-product
extends: []
related:
  - mapping
  - equivalence-relation
contrasts_with:
  - mapping

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

A relation from set $A$ to set $B$ is any subset of the Cartesian product $A \times B$.

# Core Definition

"Subsets of $A \times B$ are called relations" (Judson, p. 19). A relation associates elements of $A$ with elements of $B$ via ordered pairs, but unlike a function, a relation need not assign a unique element of $B$ to each element of $A$.

# Prerequisites

- **Cartesian product** — A relation is a subset of $A \times B$

# Key Properties

1. A relation is any subset $R \subset A \times B$
2. A relation need not assign a value to every element of $A$
3. A relation may assign multiple values to a single element of $A$
4. Functions (mappings) are special types of relations

# Construction / Recognition

## To Identify a Relation:
1. Verify it is a subset of some $A \times B$
2. It consists of ordered pairs $(a, b)$ with $a \in A$ and $b \in B$

# Context & Application

Relations generalize the concept of functions. Equivalence relations are a particularly important type of relation in algebra, used to construct quotient structures like $\mathbb{Z}_n$.

# Examples

**Example 1** (p. 20): Given $A = \{1, 2, 3\}$ and $B = \{a, b, c\}$, a relation $g$ from $A$ to $B$ that assigns $1 \mapsto a$ and $1 \mapsto b$ is a valid relation but not a mapping because 1 is assigned to two distinct elements.

# Relationships

## Builds Upon
- **cartesian-product** — Relations are subsets of Cartesian products

## Enables
- **equivalence-relation** — A special type of relation
- **mapping** — A special type of relation

## Contrasts With
- **mapping** — A mapping is a relation where each element of $A$ maps to exactly one element of $B$

# Common Errors

- **Error**: Assuming every relation is a function
  **Correction**: A relation becomes a function only when each domain element maps to exactly one codomain element

# Common Confusions

- **Confusion**: Thinking relations must be defined by formulas
  **Clarification**: A relation can be any subset of $A \times B$, defined by any means

# Source Reference

Chapter 1: Preliminaries, Section 1.2, page 19.

# Verification Notes

- Definition source: Direct from p. 19
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
