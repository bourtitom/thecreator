using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class garder_le_perso : MonoBehaviour
{
    public garder_le_perso instance;
    public GameObject player;

    public void Awake()
    {
        if (instance == null)
        {
            instance = this;
            DontDestroyOnLoad(instance);
            
        }
        else
        {
            Destroy(gameObject);
        }
    }

    public void spawn()
    {
        Transform temp = GameObject.Find("spawnhere").transform;
        Instantiate(player,temp.position,Quaternion.identity);
        
    }

    private void Update()
    {
        if(Input.GetKeyDown(KeyCode.Escape)) 
        {
            SceneManager.LoadScene("character test");
            
        }
    }
}
