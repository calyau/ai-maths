---
# === CORE IDENTIFICATION ===
concept: Subset
slug: subset

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
pdf_page: 16
section: "Sets and Equivalence Relations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - proper subset

# === TYPED RELATIONSHIPS ===
prerequisites:
  - set
extends: []
related:
  - set
  - empty-set
contrasts_with:
  - proper-subset

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
  - "What is a subset?"
---

# Quick Definition

A set $A$ is a subset of $B$, written $A \subset B$, if every element of $A$ is also an element of $B$. A proper subset is a subset that is not equal to the containing set.

# Core Definition

"A set $A$ is a subset of $B$, written $A \subset B$ or $B \supset A$, if every element of $A$ is also an element of $B$" (Judson, p. 16). A set $B$ is a **proper subset** of $A$ if $B \subset A$ but $B \neq A$. Every set is a subset of itself. Two sets are equal ($A = B$) if $A \subset B$ and $B \subset A$.

# Prerequisites

- **Set** — Subsets are defined in terms of sets and element membership

# Key Properties

1. Every set is a subset of itself: $A \subset A$
2. The empty set is a subset of every set: $\emptyset \subset A$ for all $A$
3. If $A \subset B$ and $B \subset A$, then $A = B$
4. If $A \subset B$ and $B \subset C$, then $A \subset C$ (transitivity)

# Construction / Recognition

## To Show $A \subset B$:
1. Take an arbitrary element $x \in A$
2. Show that $x \in B$

## To Show $A = B$:
1. Show $A \subset B$ (every element of $A$ is in $B$)
2. Show $B \subset A$ (every element of $B$ is in $A$)

# Context & Application

The subset relation is fundamental to defining subgroups: a subgroup $H$ of a group $G$ is a subset $H \subset G$ that is itself a group under the same operation. Proving subset containment in both directions is the standard technique for proving set equality.

# Examples

**Example 1** (p. 16): $\{4, 5, 8\} \subset \{2, 3, 4, 5, 6, 7, 8, 9\}$.

**Example 2** (p. 16): $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$.

**Example 3** (p. 16): $\{4, 7, 9\} \not\subset \{2, 4, 5, 8, 9\}$ since $7 \notin \{2, 4, 5, 8, 9\}$.

# Relationships

## Builds Upon
- **set** — Subset is a relation between sets

## Enables
- **subgroup** — A subgroup is a subset that is also a group
- **partition** — Partitions divide a set into subsets

# Common Errors

- **Error**: Concluding $A = B$ from $A \subset B$ alone
  **Correction**: Must also show $B \subset A$ to establish equality

# Common Confusions

- **Confusion**: Confusing $\in$ (element of) with $\subset$ (subset of)
  **Clarification**: $a \in A$ means $a$ is an element; $B \subset A$ means every element of $B$ is in $A$

# Source Reference

Chapter 1: Preliminaries, Section 1.2, page 16.

# Verification Notes

- Definition source: Direct quote from p. 16
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
