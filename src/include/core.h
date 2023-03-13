#ifndef CORE_H
#define CORE_H

#include <stdio.h>
#include <dirent.h>
#include <sys/stat.h>
#include <time.h>
#include <curl/curl.h>
#include <cJSON.h>

#define SUCCESS 1
#define FAILURE 0

#define MAX_UP 10

typedef unsigned char check;
typedef struct Replay
{
	char name[MAX_PATH];
	time_t play_date;
	time_t upload_date;
	check state;
} Replay;

check check_files(char dat_rt[MAX_PATH], char dir_rt[MAX_PATH]);
void wrt_file_date(char dat_rt[MAX_PATH], time_t date);
time_t get_file_date(char dat_rt[MAX_PATH]);
time_t get_dir_date(char dir_rt[MAX_PATH]);
Replay upload_replay(FILE *replay, char name[MAX_PATH]);
char *upload_all_new(time_t old_dt, char dir_rt[MAX_PATH]);
check debug_mode();

#endif