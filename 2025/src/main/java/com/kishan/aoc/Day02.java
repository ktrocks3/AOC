package com.kishan.aoc;

import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class Day02 {
    public static void main(String[] args) throws URISyntaxException, IOException {
        List<String> example = Files.readAllLines(Path.of(ClassLoader.getSystemResource("Day02/example.txt").toURI()));
        List<String> input = Files.readAllLines(Path.of(ClassLoader.getSystemResource("Day02/input.txt").toURI()));

        assert Part1(example) == 1227775554;
        System.out.println("Part 1: " + Part1(input));

        assert Part2(example) == 4174379265L;
        System.out.println("Part 2: " + Part2(input));

    }

    private static List<Long> patternGenerator(int length) {
        if (length % 2 != 0) return new ArrayList<>();
        List<Long> patterns = new ArrayList<>();
        length /= 2;
        for (int i = (int) Math.pow(10, length - 1); i < Math.pow(10, length); i++) {
            patterns.add(Long.parseLong(i + "" + i));

        }
        return patterns;
    }

    private static List<Long> patternGeneratorP2(int length) {
        HashSet<Long> patterns = new HashSet<>();

        if (length < 2) return List.of();

        // iterate over possible base lengths
        for (int baseLen = 1; baseLen <= length / 2; baseLen++) {
            if (length % baseLen != 0) continue;

            int repeats = length / baseLen;
            if (repeats < 2) continue;

            long start = (long) Math.pow(10, baseLen - 1);
            long end   = (long) Math.pow(10, baseLen);

            for (long i = start; i < end; i++) {
                String base = Long.toString(i);

                // optional but recommended: avoid non-primitive bases
                if (!isPrimitive(base)) continue;

                patterns.add(Long.parseLong(base.repeat(repeats)));
            }
        }

        return patterns.stream().toList();
    }

    private static boolean isPrimitive(String s) {
        int n = s.length();
        for (int len = 1; len <= n / 2; len++) {
            if (n % len == 0) {
                String sub = s.substring(0, len);
                if (sub.repeat(n / len).equals(s)) {
                    return false;
                }
            }
        }
        return true;
    }


    private static Long Part1(List<String> input) {
        input = List.of(input.getFirst().split(","));
        long sum = 0L;
        for (String s : input) {
            List<String> split = List.of(s.split("-"));
            String first = split.get(0);
            String second = split.get(1);
            long start = Long.parseLong(first);
            long end = Long.parseLong(second);
            List<Long> all = new ArrayList<>();
            for (int i = first.length(); i <= second.length(); i++) {
                List<Long> patterns = patternGenerator(i);
                patterns = patterns.stream().filter(item -> (start <= item) && (item <= end)).toList();
                all.addAll(patterns);
            }
            sum += all.stream().reduce(Long::sum).orElse(0L);
        }

        return sum;
    }

    private static Long Part2(List<String> input) {
        input = List.of(input.getFirst().split(","));
        long sum = 0L;
        for (String s : input) {
            List<String> split = List.of(s.split("-"));
            String first = split.get(0);
            String second = split.get(1);
            long start = Long.parseLong(first);
            long end = Long.parseLong(second);

            List<Long> all = new ArrayList<>();
            for (int i = first.length(); i <= second.length(); i++) {
                List<Long> patterns = patternGeneratorP2(i);
                patterns = patterns.stream().filter(item -> (start <= item) && (item <= end)).toList();
                all.addAll(patterns);
            }
            sum += all.stream().reduce(Long::sum).orElse(0L);
        }

        return sum;
    }
}
