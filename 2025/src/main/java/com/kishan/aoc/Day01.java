package com.kishan.aoc;

import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Day01 {
    public static void main(String[] args) throws URISyntaxException, IOException {
        List<String> example = Files.readAllLines(Path.of(ClassLoader.getSystemResource("Day01/example.txt").toURI()));
        List<String> input = Files.readAllLines(Path.of(ClassLoader.getSystemResource("Day01/input.txt").toURI()));
        assert part1(example) == 3;
        System.out.println("Part 1 answer: " + part1(input));

        assert part2(example) == 6;
        System.out.println("Part 2 answer: " + part2(input));
    }

    static int part1(List<String> input) {
        int dial = 50;
        int counter = 0;
        for (String command : input) {
            char direction = command.charAt(0);
            int distance = Integer.parseInt(command.substring(1));
            distance = direction == 'R' ? distance : -distance;
            dial = (dial + distance) % 100;
            if (dial == 0) counter++;
        }
        return counter;
    }

    static int part2(List<String> input) {
        int dial = 50;
        int counter = 0;
        for (String command : input) {
            char direction = command.charAt(0);
            int distance = Integer.parseInt(command.substring(1));
            int div, mod;
            div = Math.floorDiv(distance, 100);
            counter += div;
            mod = Math.floorMod(distance, 100);
            distance = direction == 'R' ? mod : -mod;
            if ((dial > 0 && distance < 0 && dial + distance < 0) || (distance > 0 && dial + distance > 100)) {
                counter += 1;
            }
            dial = Math.floorMod(dial + distance, 100);
            if (dial == 0) {
                counter += 1;
            }
        }
        return counter;
    }
}
