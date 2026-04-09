---
# === CORE IDENTIFICATION ===
concept: Parity Check Bit
slug: parity-check-bit

# === CLASSIFICATION ===
category: applications-coding
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Algebraic Coding Theory"
chapter_number: 8
pdf_page: 105
section: "8.1 Error-Detecting and Correcting Codes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - even parity
  - parity bit

# === TYPED RELATIONSHIPS ===
prerequisites:
  - error-detecting-code
extends: []
related:
  - block-code
  - canonical-parity-check-matrix
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a parity check bit?"
  - "How does even parity work?"
---

# Quick Definition

A parity check bit is an extra bit added to a binary word so that the total number of 1s is even (even parity) or odd (odd parity). It detects all single errors but cannot correct them.

# Core Definition

"When used for error checking, the leftmost bit is called a *parity check bit*" (Judson, p. 106). In even parity, the check bit is set to 0 or 1 so that the total number of 1s in the word is even. An $n$-tuple $\mathbf{x} = (x_1, \ldots, x_n)$ has even parity when $x_1 + x_2 + \cdots + x_n = 0$ in $\mathbb{Z}_2$.

# Prerequisites

- **Error-Detecting Code** — Even parity is the simplest error detection scheme

# Key Properties

1. Detects all single errors (changing one bit changes parity)
2. Cannot detect even numbers of simultaneous errors
3. Cannot correct any errors (only detect)
4. ASCII uses even parity: 7 information bits + 1 parity bit = 8 bits total

# Construction / Recognition

## To Add a Parity Bit:
1. Count the number of 1s in the data bits
2. If odd, set parity bit to 1; if even, set to 0
3. The total number of 1s (including parity bit) is now even

## To Check:
1. Count the total number of 1s in the received word (including parity bit)
2. If odd, an error has been detected

# Context & Application

Parity checking is the most commonly used error detection method in computers. It is used in memory (ECC RAM), communication protocols, and data storage.

# Examples

**Example 1** (p. 105-106): ASCII codes with even parity: A = 01000001 (two 1s, even), B = 01000010 (two 1s, even), C = 11000011 (four 1s, even). If A is sent and a bit flips to give 01000101 (three 1s, odd), the error is detected.

# Relationships

## Builds Upon
- **Error-Detecting Code** — Parity is the simplest form

## Enables
- **Canonical Parity-Check Matrix** — Generalizes the parity check concept

# Common Errors

- **Error**: Assuming parity bits detect multiple errors
  **Correction**: Even parity detects only an odd number of errors; two simultaneous errors go undetected

# Common Confusions

- **Confusion**: Confusing error detection with error correction
  **Clarification**: A parity bit tells you *that* an error occurred, not *where*

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.1, Example 8.3, pages 105-107.

# Verification Notes

- Definition source: Direct from p. 106
- Confidence rationale: Explicit definition with examples
- Uncertainties: None
- Cross-reference status: Verified
