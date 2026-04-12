---
concept: Abelian Group
slug: abelian-group
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.2 Groups and Subgroups"
extraction_confidence: high
aliases:
  - "commutative group"
prerequisites:
  - group
extends:
  - group
related:
  - integers-mod-n
contrasts_with: []
answers_questions:
  - "What is a group?"
---

# Quick Definition

An abelian group is a group whose law of composition is commutative: ab = ba for all elements a, b.

# Core Definition

An abelian group is a group whose law of composition is commutative (Artin, p. 52). Examples include the additive group of integers Z+, the multiplicative group of nonzero reals R*, and the group Z/nZ of integers modulo n under addition.

# Prerequisites

- **Group** — An abelian group is a group with an additional property

# Key Properties

1. ab = ba for all a, b in G
2. Every subgroup of an abelian group is normal
3. Additive notation (a + b) is typically used for abelian groups

# Construction / Recognition

## To Construct:
1. Define a group and verify commutativity

## To Recognize:
1. A group where the operation is commutative

# Context & Application

Abelian groups arise naturally in number theory (Z, Z/nZ), as additive groups of vector spaces, and as multiplicative groups of fields. Their subgroups are always normal, so quotient groups can always be formed.

# Examples

**Example 1** (p. 52): R+ (reals under addition), R* (nonzero reals under multiplication), C*, Z+.

**Example 2** (p. 52): GL_n is NOT abelian for n >= 2.

# Relationships

## Builds Upon
- **Group** — An abelian group is a commutative group

## Enables
- Every subgroup is automatically normal, so quotient groups exist freely

## Related
- **Integers mod n** — Z/nZ is an abelian group under addition

# Common Errors

- **Error**: Assuming GL_n is abelian
  **Correction**: GL_n is non-abelian for n >= 2; matrix multiplication is not commutative

# Common Confusions

- **Confusion**: Thinking "abelian" means "trivial" or "simple"
  **Clarification**: Abelian groups can be very complex; the classification of finitely generated abelian groups is a major theorem

# Source Reference

Chapter 2: Groups, Section 2.2, page 52.

# Verification Notes

- Definition source: Direct from p. 52
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
