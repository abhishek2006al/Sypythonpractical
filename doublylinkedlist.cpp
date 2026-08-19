#include<iostream>
#include<string>
using namespace std;

struct song
{
    string title;
    song* next;
    song* previous;
    
    song(string t){
    	title=t;
    	next=NULL;
    	previous=NULL;
	}

};

class playlist
{
private:
    song* head;
    song* tail;
    song* current;

public:
    playlist()
    {
        head = NULL;
        tail = NULL;
        current = NULL;
    }

    void addSong(string title)
    {
        song* newSong = new song(title);

        newSong->title = title;
        newSong->next = NULL;
        newSong->previous = NULL;

        if(head == NULL)
        {
            head = tail = current = newSong;
        }
        else
        {
            tail->next = newSong;
            newSong->previous = tail;
            tail = newSong;
        }
    }
    void nextSong(){
    	if(current==NULL){
    		cout<<"\nPlaylist is empty.";
    		
		}
		else if(current->next==NULL){
			cout<<"\nAlready at the last song.";
		}
		else{
			current=current->next;
			cout<<"\nNow playing:"<<current->title;
		}
	}
	void prevSong(){
		if(current==NULL){
    		cout<<"\nPlaylist is empty.";
    		
		}
		else if(current->previous==NULL){
			cout<<"\nAlready at the last song.";
		}
		else{
			current=current->previous;
			cout<<"\nNow playing:"<<current->title;
		}
		
	}
	void currentSong(){
		if(current==NULL){
			cout<<"\nPlaylist is empty.";
		}
		else{

			cout<<"\ncurrently playing:"<<current->title;
		}
	}

    void forward()
    {
        if(current != NULL && current->next != NULL)
        {
            current = current->next;
            cout << "Playing: " << current->title << endl;
        }
        else
        {
            cout << "No next song!" << endl;
        }
    }

    void backward()
    {
        if(current != NULL && current->previous != NULL)
        {
            current = current->previous;
            cout << "Playing: " << current->title << endl;
        }
        else
        {
            cout << "No previous song!" << endl;
        }
    }

    void display()
    {
        song* temp = head;

        while(temp != NULL)
        {
            cout <<temp->title<<"\n" ;
            temp = temp->next;
        }

        cout << "NULL" << endl;
    }
};

int main()
{
    playlist p;
    p.addSong("Song A");
    p.addSong("Song B");
    p.addSong("Song C");
    p.addSong("Song D");
    p.addSong("Song E");
    
    cout << "\nDisplay song:\n";
    p.display();
    cout << "\nNext song:";
    p.nextSong();
    cout << "\nprev song:";
    p.prevSong();
    cout << "\ncurrent song:";
    p.currentSong();

    cout << "\nForward Navigation:\n";
    p.forward();
    p.forward();

    cout << "\nBackward Navigation:\n";
    p.backward();

    return 0;
}