---
# === CORE IDENTIFICATION ===
concept: Identity Element Uniqueness
slug: identity-element-uniqueness

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
pdf_page: 49
section: "Basic Properties of Groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - inverse-uniqueness
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
---

# Quick Definition

The identity element in a group is unique: there is exactly one element $e$ such that $eg = ge = g$ for all $g$ in the group.

# Core Definition

**Proposition 3.17**: "The identity element in a group $G$ is unique; that is, there exists only one element $e \in G$ such that $eg = ge = g$ for all $g \in G$" (Judson, p. 49).

**Proof**: If both $e$ and $e'$ are identities, then $e = ee' = e'$.

# Prerequisites

- **Group** — This is a property of groups

# Key Properties

1. The identity is unique
2. Proof uses the identity property applied in two ways

# Context & Application

This proposition ensures that the group structure is well-defined. Without uniqueness of the identity, the inverse of an element might not be well-defined.

# Examples

**Example 1** (p. 49): If $e$ is the identity, then $ee' = e'$ (treating $e$ as identity). If $e'$ is also an identity, then $ee' = e$ (treating $e'$ as identity). So $e = e'$.

# Relationships

## Builds Upon
- **group** — Property of groups

## Related
- **inverse-uniqueness** — Inverses are also unique

# Source Reference

Chapter 3: Groups, Section 3.2, Proposition 3.17, page 49.

# Verification Notes

- Definition source: Direct quote from Proposition 3.17
- Confidence: HIGH — explicit proposition with proof
- Cross-reference status: Verified
- Uncertainties: None
