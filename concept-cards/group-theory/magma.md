---
# === CORE IDENTIFICATION ===
concept: Magma
slug: magma

# === CLASSIFICATION ===
category: group-fundamentals
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 10
section: "Definitions and examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - groupoid (older usage)

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - semigroup
  - monoid
  - group
contrasts_with:
  - group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a magma?"
  - "What is the most general algebraic structure with a binary operation?"
---

# Quick Definition

A magma is a set S together with a binary operation S x S -> S. No axioms beyond closure are required.

# Core Definition

A set S together with a mapping (a, b) -> a . b : S x S -> S is called a **magma** (Remark 1.9, p. 10).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Only requires a set and a closed binary operation
2. No associativity, no neutral element, no inverses required
3. The most general algebraic structure with a single binary operation

# Construction / Recognition

## To Construct:
1. Take any set S
2. Define any binary operation S x S -> S

## To Recognize:
1. A set with a binary operation — nothing more is required

# Context & Application

The magma is the weakest algebraic structure with a binary operation, sitting at the base of the hierarchy: magma -> semigroup -> monoid -> group. It is introduced by Milne to contextualize the group axioms.

# Examples

**Example 1** (p. 10): Any set with any binary operation is a magma.

# Relationships

## Enables
- **semigroup** — a magma with associativity
- **monoid** — a semigroup with a neutral element
- **group** — a monoid with inverses

## Contrasts With
- **group** — a group satisfies associativity, identity, and inverses; a magma satisfies none

# Common Confusions

- **Confusion**: Thinking a magma must be associative
  **Clarification**: Associativity is an additional axiom; a magma with associativity is a semigroup

# Source Reference

Chapter 1: Basic Definitions and Results, Remark 1.9, page 10.

# Verification Notes

- Definition source: Direct from Remark 1.9, p. 10
- Confidence rationale: HIGH — explicitly defined
- Uncertainties: None
- Cross-reference status: Verified against planned cards
