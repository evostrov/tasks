# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
# https://leetcode.com/problems/regular-expression-matching/

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Note:

# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
# Example 1:

# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:

# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
# Example 5:

# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false

# Input:
# s = "aa"
# p = "aa.*"
# Output: true

use strict;
use warnings;

use Data::Dumper;

my $string = <STDIN>;
my $pattern = <STDIN>;

chomp $string;
chomp $pattern;

my $i = 0;
my $j = 0;
my $res = 1;
while ($res && $j < length($pattern)) {
	my $p = substr($pattern, $j++, 1);

	# В случае если pattern длиннее чем string - не читаем лишние символы
	# но делать проверки все равно нужно, можеть быть такая ситуация
	# string  - ab
	# pattern - ab.*
	# это должно быть true
	my $s;
	$s = substr($string, $i++, 1) if $i < length($string);

	my $star_mod;
	if (substr($pattern, $j, 1) eq '*') {
		$j += 1;
		$star_mod = 1;
	}

	# Проверяем что символы равны
	if ($p =~ /[a-z]/) {
		$res = $res && $p eq ($s // '');
	}

	# Реализуем символ '*'
	while ($i < length($string)
		&& $res && $star_mod 		# Если символы равны и если есть '*' - надо проверить что могут быть еще такие символы
		&& (substr($string, $i, 1) eq $p || $p eq '.') # а также может быть любой символ если '.*'
	) {
		$i += 1;
	}

	# Если они были не равны то проверим есть ли '*'
	# это может значить что символ не обязательно должен быть во входной строке
	$res = $res || $star_mod;
}

# Если во входной строке остались неразобранные символы это false
$res = $res && $i == length($string);

print( ($res ? 'true' : 'false') . "\n" );
