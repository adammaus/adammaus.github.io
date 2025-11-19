---
layout: post
title: Cosine Similarity in MS SQL
date: 2012-06-20T11:46:35-05:00
excerpt: Cosine similarity measures the angle between two vectors and can be used to perform similarity between text strings. In the following code, the two input strings are vectorized and the similarity is returned as a floating point value between 0 and 1.
permalink: 2012/06/cosine-similarity-in-ms-sql/
tags:
  - MS SQL
  - Cosine Similarity
---
[Cosine similarity](http://en.wikipedia.org/wiki/Cosine_similarity) measures the angle between two vectors and can be used to perform similarity between text strings. In the following code, the two input strings are vectorized and the similarity is returned as a floating point value between 0 and 1.

{% highlight sql %}
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Description: Cosine Similarity: http://en.wikipedia.org/wiki/Cosine_similarity
-- Determines the angle between two vectors
-- =============================================
CREATE FUNCTION [dbo].[cosine_distance]
(
	@s nvarchar(4000), @t nvarchar(4000)
)
RETURNS float
AS
BEGIN
	-- Create an array of letter frequencies using the unicode of @s and @t
	DECLARE @sLet table(letter int, freq int) -- Pretend these are vectors
	DECLARE @tLet table(letter int, freq int)
	DECLARE @i int, @j int
	DECLARE @c int -- The current character

	-- Create the arrays
	SET @i = 1
	WHILE @i <= LEN(@s)
	BEGIN
		-- Use the UNICODE values for the character but not necessary
		SET @c = UNICODE(SUBSTRING(@s, @i, 1)) + 1

		-- Determine whether this character is in the vector already
		SELECT @j = COUNT(letter) FROM @sLet WHERE letter = @c
		IF @j > 0 BEGIN
			UPDATE @sLet SET freq += 1 WHERE letter = @c
		END ELSE BEGIN
			INSERT INTO @sLet VALUES (@c, 1)
		END

		-- We want to keep @tLet consistent with @sLet so insert a 0 for that letter
		SELECT @j = COUNT(letter) FROM @tLet WHERE letter = @c
		IF @j = 0 BEGIN
			INSERT INTO @tLet VALUES (@c, 0)
		END

		SELECT @i += 1
	END

	SET @i = 1
	WHILE @i <= LEN(@t)
	BEGIN
		SET @c = UNICODE(SUBSTRING(@t, @i, 1)) + 1
		SELECT @j = COUNT(letter) FROM @tLet WHERE letter = @c

		IF @j > 0 BEGIN
			UPDATE @tLet SET freq += 1 WHERE letter = @c
		END ELSE BEGIN
			INSERT INTO @tLet VALUES (@c, 1)
		END

		-- We want to keep @sLet consistent with @tLet so insert a 0 for that letter
		SELECT @j = COUNT(letter) FROM @sLet WHERE letter = @c
		IF @j = 0 BEGIN
			INSERT INTO @sLet VALUES (@c, 0)
		END

		SELECT @i += 1
	END

	-- Compute the similarity
	-- Declare the numerator for the similarity
	DECLARE @numer float
	SET @numer = 0
	SELECT @numer += s.freq * t.freq FROM @sLet s LEFT JOIN @tLet t ON s.letter = t.letter

	-- Declare the norm values and calculate the denominator for the similarity
	DECLARE @sNorm int, @tNorm int
	SET @sNorm = 0
	SET @tNorm = 0

	SELECT @sNorm += freq * freq FROM @sLet
	SELECT @tNorm += freq * freq FROM @tLet

	DECLARE @denom float
	SET @denom = SQRT(@sNorm) * SQRT(@tNorm)
	RETURN (@numer) / (@denom+1) -- The +1 eliminates the possibility 0 = @denom
END
{% endhighlight %}

To "install" this script using Microsoft SQL Server Management Studio, go to your database, and open Programmability > Functions and right-click on Scalar-valued Functions to add a new function.