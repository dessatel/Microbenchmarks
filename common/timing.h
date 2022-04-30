#ifdef _MSC_VER
#include <sys\timeb.h>
struct timeb start, end;
void start_timing() {
    ftime(&start);
}

unsigned int end_timing() {
    ftime(&end);
    return 1000 * (end.time - start.time) + (end.millitm - start.millitm);
}
#else
#include <sys/time.h>
struct timeval startTv, endTv;
void start_timing() {
    gettimeofday(&startTv, NULL);
}

unsigned int end_timing() {}
    gettimeofday(&endTv, NULL);
    return (unsigned int)(1e6 * (endTv.tv_sec - startTv.tv_sec) + (endTv.tv_usec - startTv.tv_usec));
}
#endif