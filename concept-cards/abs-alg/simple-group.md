---
concept: Simple Group
slug: simple-group
category: group-theory
subcategory: structure-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Quotient Groups and Homomorphisms"
chapter_number: 3
pdf_page: 73
section: "3.4 Composition Series and the Holder Program"
extraction_confidence: high
aliases: []
prerequisites:
  - normal-subgroup
extends: []
related:
  - composition-series
  - holder-program
  - alternating-group
contrasts_with: []
answers_questions:
  - "What is a simple group?"
  - "Why are simple groups important?"
---

# Quick Definition
A group G is simple if $|G| > 1$ and the only normal subgroups of G are $\{1\}$ and G. Simple groups are the "atoms" of group theory, analogous to primes in number theory.

# Core Definition
A group G is *simple* if $|G| > 1$ and the only normal subgroups of G are 1 and G. Every abelian simple group is $\cong Z_p$ for some prime p. There exist non-abelian simple groups; the smallest has order 60 ($A_5$). The classification of finite simple groups was completed in 1980 (Dummit & Foote, pp. 103-105).

# Prerequisites
- **Normal subgroup** — simple groups have no nontrivial normal subgroups

# Key Properties
1. Groups of prime order are simple (by Lagrange's Theorem)
2. Every abelian simple group is $\cong Z_p$
3. $A_n$ is simple for $n \geq 5$
4. Simple groups cannot be "factored" into smaller pieces via normal subgroups
5. The classification theorem lists 18 infinite families and 26 sporadic groups

# Context & Application
Simple groups play the role of primes in the "arithmetic" of groups. The Holder Program seeks to classify all finite groups by (1) classifying simple groups and (2) understanding how to assemble groups from simple composition factors.

# Examples
**Example 1** (p. 103): $Z_p$ for any prime p is simple (and abelian).
**Example 2** (p. 105): $A_5$ (order 60) is the smallest non-abelian simple group.
**Example 3** (p. 105): $SL_n(\mathbb{F})/Z(SL_n(\mathbb{F}))$ forms a family of simple groups (with small exceptions).

# Relationships
## Builds Upon
- **normal-subgroup**

## Enables
- **composition-series** — composition factors are simple groups
- **holder-program** — classifying simple groups is step 1

## Related
- **alternating-group** — $A_n$ is simple for $n \geq 5$

# Source Reference
Chapter 3, Section 3.4, pages 103-106.

# Verification Notes
- Definition source: direct from source p. 103
- Confidence rationale: explicitly defined
- Uncertainties: none
- Cross-reference status: verified
