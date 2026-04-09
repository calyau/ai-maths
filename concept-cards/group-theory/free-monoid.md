---
# === CORE IDENTIFICATION ===
concept: Free Monoid
slug: free-monoid

# === CLASSIFICATION ===
category: free-groups-presentations
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Free Groups and Presentations; Coxeter Groups"
chapter_number: 2
pdf_page: 30
section: "Free monoids"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - monoid
extends:
  - monoid
related:
  - word
  - free-group
contrasts_with:
  - free-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a free monoid?"
  - "How are words used to build free monoids?"
---

# Quick Definition

The free monoid $S_X$ on a set $X$ is the monoid of all finite words (sequences of symbols) from $X$, with juxtaposition as the binary operation and the empty word as identity.

# Core Definition

"Write $S_X$ for the set of words together with this binary operation [juxtaposition]. Then $S_X$ is a monoid, called the *free monoid* on $X$." (Milne, p. 31)

$S_X$ has the universal property: for any map $\alpha: X \to S$ to a monoid $S$, there exists a unique monoid homomorphism $S_X \to S$ extending $\alpha$.

# Prerequisites

- **Monoid** — a set with an associative binary operation and identity

# Key Properties

1. Elements are finite sequences (words) of symbols from $X$
2. Multiplication is juxtaposition (concatenation)
3. The empty sequence $1$ is the identity
4. $X$ generates $S_X$ (no proper submonoid contains $X$)
5. Universal property: maps from $X$ extend uniquely to monoid homomorphisms from $S_X$

# Context & Application

The free monoid is the precursor to the free group. Free groups are constructed by starting with the free monoid on $X' = \{a, a^{-1}, b, b^{-1}, \ldots\}$ and adding cancellation.

# Examples

**Example 1** (p. 31): Words on $X = \{a, b, c\}$ include $aaaa$, $aabac$, etc. The product $aaaa \cdot aabac = aaaaaabac$.

# Relationships

## Builds Upon
- **monoid**

## Enables
- **free-group** — constructed from the free monoid by adding inverses and cancellation

## Contrasts With
- **free-group** — the free monoid has no inverses

# Source Reference

Chapter 2, page 31.

# Verification Notes

- Definition source: Direct from p. 31
- Confidence: HIGH — explicit definition
- Uncertainties: None
