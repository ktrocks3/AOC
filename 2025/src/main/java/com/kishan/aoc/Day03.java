package com.kishan.aoc;

import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Day03 {
    public static void main(String[] args) throws URISyntaxException, IOException {

        List<String> example = Files.readAllLines(Path.of(ClassLoader.getSystemResource("Day03/example.txt").toURI()));
        List<String> input = Files.readAllLines(Path.of(ClassLoader.getSystemResource("Day03/input.txt").toURI()));

        assert Part1(example) == 357;
        System.out.println("Part 1: " + Part1(input));

        assert Part2(example) == 3121910778619L;
        System.out.println("Part 2: " + Part2(input));

    }

    private static int highestNum(String s) {
        int x = -1;
        int index = -1;
        for (int i = 0; i < s.length(); i++) {
            int si = Integer.parseInt(s.charAt(i) + "");
            if (x < si) {
                x = si;
                index = i;
            }
        }
        return index;
    }

    private static int Part1(List<String> input) {
        int sum = 0;
        for (String s : input) {
            int index1 = highestNum(s.substring(0, s.length()-1));
            int index2 = highestNum(s.substring(index1+1)) + index1 + 1;
            sum += Integer.parseInt(s.charAt(index1) + "" + s.charAt(index2));
        }

        return sum;
    }

    private static long Part2(List<String> input) {
        long sum = 0;
        for (String s : input) {
            int previous = highestNum(s.substring(0, s.length()-11));
            StringBuilder res = new StringBuilder(s.charAt(previous) + "");
            for (int i = 10; i >= 0; i--) {
                int index = highestNum(s.substring(previous+1, s.length()-i)) + previous + 1;
                previous=index;
                res.append(s.charAt(index));
            }
            sum += Long.parseLong(String.valueOf(res));
        }

        return sum;
    }
}
