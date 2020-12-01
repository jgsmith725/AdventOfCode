def main():
    recipe_count = 360781

    scores = [3, 7]
    elf_1_idx = 0
    elf_2_idx = 1

    done = False
    cnt = 0
    while not done:
        new_score = str(scores[elf_1_idx] + scores[elf_2_idx])

        for char in new_score:
            scores.append(int(char))

        elf_1_idx = (elf_1_idx + scores[elf_1_idx] + 1) % len(scores)
        elf_2_idx = (elf_2_idx + scores[elf_2_idx] + 1) % len(scores)

        #part 1
        #if len(scores) >= recipe_count + 10:
        #    done = True
        #    output = ''
        #    for idx in range(recipe_count, recipe_count + 10):
        #        output += str(scores[idx])
        #    print(output)

        
        
        # score_search = [3,6,0,7,8,1]
        # start_search_idx = len(scores) - len(score_search)
        # if start_search_idx >= 0:
        #     done = True
        #     for idx in range(len(score_search)):
        #         if not score_search[idx] == scores[len(scores) - len(score_search) + idx]:
        #             done = False
        #             break
        #     if done == True:
        #         print('found after recipes: ' + str(len(scores) - len(score_search)))
        #         #print(scores)
        #         break

        #     done = True
        #     for idx in range(len(score_search)):
        #         if not score_search[idx] == scores[len(scores) - len(score_search) + idx - 1]:
        #             done = False
        #             break
        #     if done == True:
        #         print('found after recipes: ' + str(len(scores) - len(score_search) - 1))
        #         #print(scores)
        #         break


        cnt += 1
        if cnt % 100000 == 0:
            print(str(cnt) + ' ' + str(len(scores)))
        if cnt > 20000000:
            break
if __name__== "__main__":
    main()