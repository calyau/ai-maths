---
concept: Normalizer
slug: normalizer
category: group-theory
subcategory: conjugation
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "More Group Theory"
chapter_number: 7
pdf_page: 206
section: "7.6 Normalizers"
extraction_confidence: high
aliases:
  - "N(H)"
prerequisites:
  - conjugation
  - stabilizer
extends:
  - stabilizer
related:
  - normal-subgroup
  - sylow-p-subgroup
  - centralizer
contrasts_with:
  - centralizer
answers_questions:
  - "What is the normalizer of a subgroup?"
  - "What distinguishes a normal subgroup from a general subgroup?"
---

# Quick Definition

The normalizer N(H) of a subgroup H is the largest subgroup of G in which H is normal: N(H) = {g in G | gHg^{-1} = H}. The number of conjugate subgroups equals [G : N(H)].

# Core Definition

The normalizer of H is the stabilizer of [H] for the operation of conjugation by G on its subgroups: N(H) = {g in G | gHg^{-1} = H} (Artin, (7.6.1), p. 216). The Counting Formula gives |G| = |N(H)| * (number of conjugate subgroups), with the number of conjugates equal to [G : N(H)] (7.6.2).

# Prerequisites

- **Conjugation** — Normalizer is the stabilizer for conjugation on subgroups
- **Stabilizer** — N(H) is a special case

# Key Properties

1. N(H) = {g | gHg^{-1} = H}
2. H is normal in N(H) (Proposition 7.6.3(a))
3. H is normal in G iff N(H) = G (Proposition 7.6.3(b))
4. |H| divides |N(H)| and |N(H)| divides |G| (Proposition 7.6.3(c))
5. Number of conjugates of H = [G : N(H)]

# Construction / Recognition

## To Compute:
1. Find all g such that gHg^{-1} = H
2. These form the normalizer N(H)

# Context & Application

Normalizers are essential in the Sylow theorems: the number of Sylow p-subgroups is [G : N(H)] where H is one such subgroup. The normalizer is the natural setting where a subgroup becomes normal.

# Examples

**Example 1** (p. 216): In S_5, let H = <(12)(34)> (order 2). The conjugacy class of (12)(34) has 15 elements, each generating a conjugate of H. So N(H) has order 120/15 = 8.

# Relationships

## Builds Upon
- **Stabilizer** — N(H) is the stabilizer for conjugation on subgroups

## Enables
- **Sylow theorems** — Number of Sylow subgroups = [G : N(H)]

## Related
- **Normal subgroup** — H is normal iff N(H) = G

## Contrasts With
- **Centralizer** — Z(x) stabilizes an element; N(H) stabilizes a subgroup

# Source Reference

Chapter 7: More Group Theory, Section 7.6, (7.6.1)-(7.6.2), Proposition 7.6.3, pages 216-217.

# Verification Notes

- Definition source: Direct from (7.6.1)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
