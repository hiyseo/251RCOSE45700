#include <stdio.h>
int main() {
    int n, bt[10], wt[10], tat[10];
    float avg_wt=0, avg_tat=0;
    printf("프로세스 수: "); scanf("%d", &n);
    for(int i=0;i<n;i++) {
        printf("P%d BT: ",i+1); scanf("%d",&bt[i]);
    }
    wt[0]=0;
    for(int i=1;i<n;i++) wt[i]=wt[i-1]+bt[i-1];
    for(int i=0;i<n;i++) {
        tat[i]=wt[i]+bt[i];
        avg_wt += wt[i]; avg_tat += tat[i];
    }
    printf("\nP\tBT\tWT\tTAT\n");
    for(int i=0;i<n;i++)
        printf("P%d\t%d\t%d\t%d\n",i+1,bt[i],wt[i],tat[i]);
    printf("\nAvg WT=%.2f, Avg TAT=%.2f\n",avg_wt/n,avg_tat/n);
    return 0;
}