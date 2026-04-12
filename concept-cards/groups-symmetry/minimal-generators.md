---
# === CORE IDENTIFICATION ===
concept: Minimal Set of Generators
slug: minimal-generators

# === CLASSIFICATION ===
category: abelian-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Finitely Generated Abelian Groups"
chapter_number: 21
pdf_page: 126
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "minimal generating set"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - finitely-generated-abelian-group
extends: []
related:
  - classification-of-fg-abelian-groups
  - relation-between-generators
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a minimal set of generators for a finitely generated abelian group?"
  - "How can generators be changed while preserving the group?"
---

# Quick Definition

A minimal set of generators $x_1, \ldots, x_r$ for a finitely generated abelian group $G$ is one where no set of $r - 1$ elements can generate $G$. The generators can be changed (e.g., replacing $x_1$ by $x_1 x_2^q$) without changing the group.

# Core Definition

Let $G$ be a finitely generated abelian group and let $x_1, \ldots, x_r$ be distinct elements which together generate $G$. If no set of $r - 1$ elements can generate $G$, we call $x_1, \ldots, x_r$ a **minimal set of generators** (Armstrong, p. 127).

Because the group is abelian, each $g \in G$ can be written as $g = x_1^{n_1} x_2^{n_2} \cdots x_r^{n_r}$. The set $x_1 x_2^q, x_2, \ldots, x_r$ is also a minimal set of generators for any integer $q$ (p. 127).

# Prerequisites

- **Finitely generated abelian group** -- the setting for minimal generators

# Key Properties

1. In an abelian group, every element can be written as a product of powers of generators (collecting terms)
2. Replacing $x_1$ by $x_1 x_2^q$ for any integer $q$ preserves minimality
3. More generally, any invertible integer-coefficient change of generators is valid
4. These generator changes correspond to column operations on the relation matrix (Chapter 22)

# Context & Application

The concept of minimal generators is essential for the proof of Theorem 21.1. The proof works by finding a minimal set of generators with the simplest possible relations, achieved through systematic generator changes.

# Relationships

## Builds Upon
- **Finitely generated abelian group** -- the context

## Enables
- **Classification of f.g. abelian groups** -- the proof systematically simplifies generators and relations

## Related
- **Relation between generators** -- generators are linked by relations
- **Smith normal form** -- column operations correspond to generator changes

# Source Reference

Chapter 21: Finitely Generated Abelian Groups, page 127.

# Verification Notes

- Definition: Direct from p. 127
- Generator change: Explicit on p. 127
- Confidence: HIGH -- clearly defined
