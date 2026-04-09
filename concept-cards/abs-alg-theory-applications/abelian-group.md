---
# === CORE IDENTIFICATION ===
concept: Abelian Group
slug: abelian-group

# === CLASSIFICATION ===
category: group-theory
subcategory: group-properties
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Groups"
chapter_number: 3
pdf_page: 47
section: "Definitions and Examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - commutative group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends:
  - group
related:
  - cyclic-group
contrasts_with:
  - nonabelian-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
  - "What distinguishes abelian from nonabelian groups?"
---

# Quick Definition

An abelian (or commutative) group is a group $G$ where the operation is commutative: $a \circ b = b \circ a$ for all $a, b \in G$.

# Core Definition

"A group $G$ with the property that $a \circ b = b \circ a$ for all $a, b \in G$ is called abelian or commutative" (Judson, p. 47).

# Prerequisites

- **Group** — An abelian group is a group with an additional property

# Key Properties

1. $ab = ba$ for all $a, b \in G$
2. Every cyclic group is abelian (Theorem 4.9)
3. In an abelian group, $(gh)^n = g^n h^n$ (Theorem 3.23)
4. Named after Niels Henrik Abel

# Construction / Recognition

## To Verify a Group is Abelian:
1. Confirm it is a group
2. Show $ab = ba$ for all $a, b \in G$
3. Alternatively, show $aba^{-1}b^{-1} = e$ for all $a, b$

# Context & Application

Abelian groups are simpler to study than nonabelian groups. The classification of finite abelian groups is a major theorem in algebra. Many familiar groups are abelian: $(\mathbb{Z}, +)$, $(\mathbb{Z}_n, +)$, $(\mathbb{Q}^*, \cdot)$, $(\mathbb{R}^*, \cdot)$.

# Examples

**Example 1** (p. 47): $(\mathbb{Z}, +)$ is abelian since $m + n = n + m$.

**Example 2** (p. 47): $(\mathbb{Z}_5, +)$ is abelian.

**Non-Example** (p. 48): $GL_2(\mathbb{R})$ is NOT abelian since matrix multiplication is not commutative.

# Relationships

## Builds Upon
- **group** — An abelian group is a group with commutativity

## Related
- **cyclic-group** — Every cyclic group is abelian

## Contrasts With
- **nonabelian-group** — Groups where $ab \neq ba$ for some elements

# Common Errors

- **Error**: Assuming all groups are abelian
  **Correction**: Many important groups (e.g., $S_3$, $GL_n(\mathbb{R})$, $Q_8$) are nonabelian

# Common Confusions

- **Confusion**: Thinking abelian means "simple" or "trivial"
  **Clarification**: Abelian groups can have rich structure; the classification of finite abelian groups is a deep theorem

# Source Reference

Chapter 3: Groups, Section 3.2, page 47.

# Verification Notes

- Definition source: Direct quote from p. 47
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
