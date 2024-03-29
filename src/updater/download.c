#include <auto_updater.h>

bool download()
{
	bool result = true;
	printf("Downloading update...\n\n");
	curl_global_init(CURL_GLOBAL_DEFAULT);
	CURL *handle = curl_easy_init();
	if (!handle)
	{
		perror("\n[!] Curl init failed\n");
		result = false;
		goto cleanup;
	}
	FILE *outfile;
	outfile = fopen("temp.zip", "wb");

	curl_easy_setopt(handle, CURLOPT_URL, UPDATE_ENDPOINT);
	curl_easy_setopt(handle, CURLOPT_FOLLOWLOCATION, 1L);
	curl_easy_setopt(handle, CURLOPT_WRITEDATA, outfile);
	curl_easy_setopt(handle, CURLOPT_WRITEFUNCTION, write_callback);

	curl_easy_setopt(handle, CURLOPT_VERBOSE, 1L);
	CURLcode res = curl_easy_perform(handle);

	fclose(outfile);
	if (res != CURLE_OK)
	{
		fprintf(stderr, "[!] Curl perform failed: %s\n", curl_easy_strerror(res));
		result = false;
		goto cleanup;
	}

	long http_code = 0;
	curl_easy_getinfo(handle, CURLINFO_RESPONSE_CODE, &http_code);
	if (http_code > 299)
	{
		printf("\n[!] HTTP failure - %ld\n", http_code);
		result = false;
		goto cleanup;
	}

	cleanup:
		curl_global_cleanup();
		curl_easy_cleanup(handle);

	return result;
}

size_t write_callback(void *ptr, size_t size, size_t nmemb, void *stream)
{
	size_t written = fwrite(ptr, size, nmemb, (FILE *)stream);
	return written;
}