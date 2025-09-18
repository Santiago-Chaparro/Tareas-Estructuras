import java.util.Scanner;
public class Main{
    public static void main(String[]a){
        char[][]t=new char[6][7];
        for(int i=0;i<6;i++)for(int j=0;j<7;j++)t[i][j]='.';
        Scanner sc=new Scanner(System.in);
        char j='X';boolean g=false;
        while(!g){
            mostrar(t);
            System.out.print("Turno "+j+" (0-6): ");
            int c=sc.nextInt(),f=-1;
            for(int i=5;i>=0;i--)if(t[i][c]=='.'){f=i;break;}
            if(f==-1){System.out.println("Llena");continue;}
            t[f][c]=j;
            if(gana(t,f,c,j)){mostrar(t);System.out.println("¡Jugador "+j+" gana!");g=true;}
            j=(j=='X')?'O':'X';
        }
        sc.close();
    }
    static void mostrar(char[][]t){
        for(int i=0;i<6;i++){for(int j=0;j<7;j++)System.out.print(t[i][j]+" ");System.out.println();}
        System.out.println("0 1 2 3 4 5 6");
    }
    static boolean gana(char[][]t,int f,int c,char j){
        int[][]d={{1,0},{0,1},{1,1},{1,-1}};
        for(int[]v:d)if(1+contar(t,f,c,v[0],v[1],j)+contar(t,f,c,-v[0],-v[1],j)>=4)return true;
        return false;
    }
    static int contar(char[][]t,int f,int c,int df,int dc,char j){
        int n=0,i=f+df,k=c+dc;
        while(i>=0&&i<6&&k>=0&&k<7&&t[i][k]==j){n++;i+=df;k+=dc;}
        return n;
    }
}
