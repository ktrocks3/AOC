package com.kishan.aoc;

import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;

public class Day06 {

    public static void main(String[] args) throws URISyntaxException, IOException {
        List<String> example = Files.readAllLines(Path.of(ClassLoader.getSystemResource("Day06/example.txt").toURI()));
        List<String> input = Files.readAllLines(Path.of(ClassLoader.getSystemResource("Day06/input.txt").toURI()));

        assert Part1(example) == 4277556;
        System.out.println("Part 1: " + Part1(input));

        example = Files.readAllLines(Path.of(ClassLoader.getSystemResource("Day06/example.txt").toURI()));
        input = Files.readAllLines(Path.of(ClassLoader.getSystemResource("Day06/input.txt").toURI()));
        assert Part2(example) == 3263827;
        System.out.println("Part 2: " + Part2(input));

    }



    private static long Part1(List<String> input) {
        String[] ops = input.removeLast().trim().split("\\s+");
        long[] ans = Arrays.stream(input.removeFirst().trim().split("\\s+")).mapToLong(Long::parseLong).toArray();
        for (String line : input) {
            String[] nums = line.trim().split("\\s+");
            for (int i = 0; i < nums.length; i++) {
                if (Objects.equals(ops[i], "+")) {
                    ans[i] += Long.parseLong(nums[i]);
                } else if (Objects.equals(ops[i], "*")) {
                    ans[i] *= Long.parseLong(nums[i]);

                }
            }
        }
        return Arrays.stream(ans).sum();
    }

    static List<String> splitAtIndexes(String s, List<Integer> indexes) {
        List<String> result = new ArrayList<>();

        int prev = 0;
        for (int idx : indexes) {
            result.add(s.substring(prev, idx));
            prev = idx;
        }
        result.add(s.substring(prev));

        return result;
    }


    private static long Part2(List<String> input) {
        List<Integer> separators = new ArrayList<>();
        String operators = input.removeLast();
        for (int i = 1; i < operators.length(); i++) {
            if (operators.charAt(i) != ' ') {
                separators.add(i-1);
            }
        }
        String[] ops = operators.trim().split("\\s+");

        int rows = input.size();
        int cols = separators.size()+1;

        String[][] nums = new String[rows][cols];
        String[][] transposed = new String[cols][rows];
        for (int i = 0; i < input.size(); i++) {
            nums[i] = splitAtIndexes(input.get(i), separators).toArray(new String[0]);
        }

        for (int i = 0; i < cols; i++) {
            for (int j = 0; j < rows; j++) {
                transposed[i][j] = new StringBuilder(nums[j][i]).reverse().toString();
            }
        }

        long[] ans = new long[ops.length];
        for (int i = 0; i < ops.length; i++) {
            if (Objects.equals(ops[i], "+")) {
                ans[i] = 0;
            } else if (Objects.equals(ops[i], "*")) {
                ans[i] = 1;
            }
        }

        for (int i = 0; i < transposed.length; i++) {
            String[] strings = transposed[i];
            int slen = 0;
            for (String string : strings) {
                slen = Math.max(slen, string.length());
            }
            String[] converted = new String[slen];
            Arrays.fill(converted, "");
            for (String string : strings) {
                for (int j = 0; j < string.length(); j++) {
                    converted[j] += string.charAt(j);
                }
            }

            if (Objects.equals(ops[i], "+")) {
                for (String s : converted) {
                    s = s.trim();
                    if (s.isEmpty()) continue;
                    ans[i] += Long.parseLong(s);
                }
            } else if (Objects.equals(ops[i], "*")) {
                for (String s : converted) {
                    s = s.trim();
                    if (s.isEmpty()) continue;
                    ans[i] *= Long.parseLong(s);
                }
            }
        }

        return Arrays.stream(ans).sum();
    }
}
